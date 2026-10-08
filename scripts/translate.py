#!/usr/bin/env python3
"""Traduz automaticamente os arquivos de idioma do GTLAdditions via API DeepSeek.

Cobertura:
  - assets/*/lang/en_us.json  <->  zh_cn.json          (strings do jogo)
  - assets/*/lang/pt_br.json  <- consenso en/zh         (strings do jogo)
  - assets/gtladditions/guides/**/guide/**.md          (guias GuideME)
      raiz = ingles (fonte)  |  _zh_cn/ = chines simplificado (espelho)
      _pt_br/ = portugues brasileiro (derivado do consenso en/zh)

Regras:
  - Ingles e' a fonte de verdade. Entradas novas/alteradas sao re-traduzidas;
    entradas que so existem no chines sao traduzidas de volta para o ingles.
    Para evitar loops de retraducao, so o par en_us<->zh_cn e' sincronizado
    bidirecionalmente (adicione outros idiomas editando abaixo).
  - Pipeline de desambiguacao em duas etapas:
      1. en_us <-> zh_cn e' sincronizado PRIMEIRO para convergir num termo
         canonico contextual (ex.: "casting" pode ser 铸造, 浇铸 ou 铸件;
         o alinhamento resolve qual e' o correto naquele contexto).
      2. So depois o pt_br e' traduzido, recebendo o texto em ingles E o
         chines ja consensuado como referencia de desambiguacao.
  - A traducao recebe CONTEXTO: glossario do mod + amostras de pares ja
    traduzidos do mesmo arquivo, para manter termos coesos entre versoes.
  - Entradas existentes NAO sao retraduzidas: so o que mudou (hash do texto
    fonte gravado em *.hashes / *.srchash) e' enviado a API, mantendo a
    coesao com as traducoes anteriores.
  - Markdown: o front-matter YAML so tem `navigation.title` traduzido; tags
    como <Row>, <BlockImage id="..."/>, <Color> e links .md ficam intactas.
    O corpo e' dividido em blocos semanticos (paragrafos, tabelas e blocos
    de tags GuideME nunca sao cortados no meio).

Requer: variavel de ambiente DEEPSEEK_API_KEY.
Uso:    python3 scripts/translate.py            (aplica as traducoes; saida 0)
        python3 scripts/translate.py --check    (so verifica se ha pendencias)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"
DEEPSEEK_MODEL = "deepseek-chat"
MAX_RETRIES = 4

# Pares de idiomas sincronizados bidirecionalmente (fonte, destino).
LANG_PAIRS = [("en_us", "zh_cn")]

# Idioma gerado na etapa 2, a partir do consenso en_us <-> zh_cn.
PT_BR = "pt_br"

# Diretorios de lang que entram na sincronizacao.
LANG_DIRS = [
    "src/main/resources/assets/gtladditions/lang",
    "src/main/resources/assets/gtceu/lang",
]

# Guias GuideME: raiz (ingles) espelhada em _zh_cn/ e _pt_br/.
GUIDE_ROOT = "src/main/resources/assets/gtladditions/guides/gtladditions/guide"
GUIDE_MIRROR_DIR = "_zh_cn"
PTBR_GUIDE_MIRROR_DIR = "_pt_br"

# Diretorios-espelho (nao sao fontes de traducao).
GUIDE_MIRROR_DIRS = {GUIDE_MIRROR_DIR, PTBR_GUIDE_MIRROR_DIR}

MAX_ENTRIES_PER_CALL = 80
MD_MAX_CHARS_PER_CALL = 6000
MD_REF_MAX_CHARS = 4000

GLOSSARY = """\
- Mod: GTLAdditions, addon de GregTech Leisure / GregTech CEu (GTLCore).
- Circuit: Circuit (NAO "program"). Computation/Computation power: Computational Power/CWUt.
- Multiblock: Multiblock. Hatch: Hatch. Coil: Coil. Recipe: Recipe.
- Mantenha nomes de mods (GregTech, AE2, Applied Energistics 2, GuideME) e nomes proprios de maquinas com a grafia consagrada do zh_cn.
- NUNCA traduza: placeholders %s %1$s %d %%d, codigos de cor §a §6 §c §r, ids snake_case (ex.: biosphere_iii), caminhos .md, comandos /..., tags XML/HTML, nomes de mods.
"""

LANG_SYSTEM_PROMPT = """\
You are a professional localization translator for the Minecraft mod "GTLAdditions".
Translate game strings between English (en_us) and Simplified Chinese (zh_cn).

CONTEXT / GLOSSARY:
{glossary}

STRICT RULES:
1. The input is a JSON object mapping stable ids to texts in the SOURCE language. {direction}
2. Return ONLY a JSON object with EXACTLY the same ids, values translated.
3. Keep every placeholder (%s, %1$s, %d), Minecraft formatting code (§ + char) and newline (\\n) exactly where they belong.
4. Be consistent with the glossary and with the surrounding context lines provided in the user message.
5. No commentary, no markdown fences — raw JSON only.
"""

LANG_PTBR_SYSTEM_PROMPT = """\
You are a professional localization translator for the Minecraft mod "GTLAdditions".
Translate game strings from English (en_us) to Brazilian Portuguese (pt_br).

For each entry you receive BOTH the English source and the Simplified Chinese
(zh_cn) translation. The zh_cn is the result of a context-disambiguation pass:
use it ONLY to resolve ambiguous English words, but write idiomatic Brazilian
Portuguese (Minecraft community terms), never a literal translation of the Chinese.

CONTEXT / GLOSSARY:
{glossary}

STRICT RULES:
1. The input is a JSON object mapping stable ids to objects like {{"en": "...", "zh": "..."}}.
2. Return ONLY a JSON object with EXACTLY the same ids, values translated to pt_br.
3. Keep every placeholder (%s, %1$s, %d), Minecraft formatting code (§ + char) and newline (\\n) exactly where they belong.
4. Be consistent with the glossary and with the surrounding context lines provided in the user message.
5. No commentary, no markdown fences — raw JSON only.
"""

MD_SYSTEM_PROMPT = """\
You are a professional localization translator for the Minecraft mod "GTLAdditions".
You translate GuideME guide pages between English (en) and Simplified Chinese (zh_cn).

CONTEXT / GLOSSARY:
{glossary}

STRICT RULES:
1. The input JSON maps stable ids to fragments of ONE markdown page. {direction}
2. Return ONLY a JSON object with the same ids, fragments translated.
3. NEVER alter: HTML/GuideME tags (<Row>, <BlockImage id="..." scale="4"/>, <Color color="#00AA00">), attribute values, markdown link targets (file.md, ../x.md), inline code, item ids in snake_case, image paths.
4. YAML front-matter fragments (ids starting with "fm:") contain only a `title:` line — translate just the title text, keep the YAML shape.
5. Keep markdown structure characters (#, *, >, |, -, list markers) untouched. Hard line breaks (trailing backslash) must be kept.
6. No commentary, no markdown fences — raw JSON only.
"""

MD_PTBR_SYSTEM_PROMPT = """\
You are a professional localization translator for the Minecraft mod "GTLAdditions".
You translate GuideME guide pages from English (en) to Brazilian Portuguese (pt_br).

You receive the English fragments AND a reference Simplified Chinese (zh_cn)
translation of the same page. The zh_cn is a context-disambiguation pass; use it
ONLY to resolve ambiguous terms, but produce idiomatic Brazilian Portuguese.

CONTEXT / GLOSSARY:
{glossary}

STRICT RULES:
1. The input JSON maps stable ids to fragments of ONE markdown page.
2. Return ONLY a JSON object with the same ids, fragments translated to pt_br.
3. NEVER alter: HTML/GuideME tags (<Row>, <BlockImage id="..." scale="4"/>, <Color color="#00AA00">), attribute values, markdown link targets (file.md, ../x.md), inline code, item ids in snake_case, image paths.
4. YAML front-matter fragments (ids starting with "fm:") contain only a `title:` line — translate just the title text, keep the YAML shape.
5. Keep markdown structure characters (#, *, >, |, -, list markers) untouched. Hard line breaks (trailing backslash) must be kept.
6. No commentary, no markdown fences — raw JSON only.
"""

# ---------------------------------------------------------------------------
# DeepSeek
# ---------------------------------------------------------------------------


def deepseek_chat(system_prompt: str, user_message: str) -> str:
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("::error::DEEPSEEK_API_KEY nao definido.", file=sys.stderr)
        sys.exit(1)

    payload = json.dumps(
        {
            "model": DEEPSEEK_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            "temperature": 0.2,
            "response_format": {"type": "json_object"},
        }
    ).encode("utf-8")

    for attempt in range(1, MAX_RETRIES + 1):
        req = urllib.request.Request(
            DEEPSEEK_URL,
            data=payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", "replace")[:300]
            retriable = exc.code in (429, 500, 502, 503, 504)
            print(f"[deepseek] HTTP {exc.code} (tentativa {attempt}): {body}", file=sys.stderr)
            if not retriable or attempt == MAX_RETRIES:
                raise
        except (urllib.error.URLError, TimeoutError) as exc:
            print(f"[deepseek] erro de rede (tentativa {attempt}): {exc}", file=sys.stderr)
            if attempt == MAX_RETRIES:
                raise
        time.sleep(5 * attempt)
    raise RuntimeError("DeepSeek: tentativas esgotadas")


def parse_json_response(raw: str) -> dict:
    raw = raw.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-zA-Z]*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw.strip())
    start, end = raw.find("{"), raw.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"resposta sem objeto JSON: {raw[:200]}")
    return json.loads(raw[start : end + 1])


def translate_map(pairs: dict[str, str], kind: str, direction: str, context: str) -> dict[str, str]:
    """Traduz {id: texto} em lotes; devolve {id: traducao}."""
    if not pairs:
        return {}
    system = (LANG_SYSTEM_PROMPT if kind == "lang" else MD_SYSTEM_PROMPT).format(
        glossary=GLOSSARY, direction=direction
    )
    out: dict[str, str] = {}
    items = list(pairs.items())
    for i in range(0, len(items), MAX_ENTRIES_PER_CALL):
        batch = dict(items[i : i + MAX_ENTRIES_PER_CALL])
        user = json.dumps(batch, ensure_ascii=False, indent=1)
        if context:
            user = f"Surrounding context (do NOT translate):\n{context}\n\nTranslate:\n{user}"
        translated = parse_json_response(deepseek_chat(system, user))
        for key in batch:
            value = translated.get(key)
            if not isinstance(value, str) or not value.strip():
                print(f"[aviso] id '{key}' sem traducao; mantendo fonte", file=sys.stderr)
                value = batch[key]
            out[key] = value
        print(f"  lote {i // MAX_ENTRIES_PER_CALL + 1}: {len(batch)} entrada(s) traduzidas")
    return out


def translate_ptbr_map(entries: dict[str, dict[str, str]], context: str) -> dict[str, str]:
    """Traduz {id: {"en": ..., "zh": ...}} para pt_br, usando o zh_cn como
    referencia de desambiguacao. Devolve {id: traducao}."""
    if not entries:
        return {}
    system = LANG_PTBR_SYSTEM_PROMPT.format(glossary=GLOSSARY)
    out: dict[str, str] = {}
    items = list(entries.items())
    for i in range(0, len(items), MAX_ENTRIES_PER_CALL):
        batch = dict(items[i : i + MAX_ENTRIES_PER_CALL])
        user = json.dumps(batch, ensure_ascii=False, indent=1)
        if context:
            user = f"Surrounding context (do NOT translate):\n{context}\n\nTranslate:\n{user}"
        translated = parse_json_response(deepseek_chat(system, user))
        for key in batch:
            value = translated.get(key)
            if not isinstance(value, str) or not value.strip():
                print(f"[aviso] id '{key}' sem traducao pt_br; mantendo fonte", file=sys.stderr)
                value = batch[key]["en"]
            out[key] = value
        print(f"  lote {i // MAX_ENTRIES_PER_CALL + 1}: {len(batch)} entrada(s) traduzidas")
    return out


def translate_ptbr_md(fragments: dict[str, str], zh_text: str) -> dict[str, str]:
    """Traduz {id: fragmento} de markdown para pt_br usando o zh_cn da mesma
    pagina como referencia de desambiguacao."""
    if not fragments:
        return {}
    system = MD_PTBR_SYSTEM_PROMPT.format(glossary=GLOSSARY)
    out: dict[str, str] = {}
    items = list(fragments.items())
    for i in range(0, len(items), MAX_ENTRIES_PER_CALL):
        batch = dict(items[i : i + MAX_ENTRIES_PER_CALL])
        user = json.dumps(batch, ensure_ascii=False, indent=1)
        if zh_text:
            user = (
                "Reference Simplified Chinese translation of the same page "
                "(for disambiguation; do NOT translate this reference):\n"
                f"{zh_text}\n\nTranslate:\n{user}"
            )
        translated = parse_json_response(deepseek_chat(system, user))
        for key in batch:
            value = translated.get(key)
            if not isinstance(value, str) or not value.strip():
                print(f"[aviso] id '{key}' sem traducao pt_br; mantendo fonte", file=sys.stderr)
                value = batch[key]
            out[key] = value
        print(f"  lote {i // MAX_ENTRIES_PER_CALL + 1}: {len(batch)} fragmento(s) traduzidos")
    return out


def sha1_text(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Lang (JSON)
# ---------------------------------------------------------------------------


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        print(f"::error::JSON invalido em {path}: {exc}", file=sys.stderr)
        sys.exit(1)


def write_lang(path: Path, data: dict, template: dict) -> None:
    """Grava o JSON seguindo a ordem das chaves do arquivo-template."""
    ordered = {k: data[k] for k in template if k in data}
    for k in data:
        if k not in ordered:
            ordered[k] = data[k]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sync_lang_file(src_path: Path, tgt_path: Path, direction: str, apply: bool) -> bool:
    """Sincroniza o arquivo-fonte (en_us) com o destino (zh_cn): chaves novas
    ou alteradas sao traduzidas; chaves apagadas da fonte sao apagadas do destino."""
    src = load_json(src_path)
    tgt = load_json(tgt_path)
    if not src:
        return False

    src_hash_file = src_path.with_suffix(src_path.suffix + f".{tgt_path.stem}.hashes")
    old_hashes: dict = {}
    if src_hash_file.exists():
        try:
            old_hashes = json.loads(src_hash_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            old_hashes = {}

    new_hashes = {k: sha1_text(str(v)) for k, v in src.items()}

    to_translate: dict[str, str] = {}
    for key, value in src.items():
        if key not in tgt or old_hashes.get(key) != new_hashes[key]:
            to_translate[key] = str(value)

    removed = [k for k in tgt if k not in src]
    if not to_translate and not removed:
        return False

    print(f"[lang] {src_path}: {len(to_translate)} para traduzir, {len(removed)} removidas")

    context = ""
    sample_keys = [k for k in src if k not in to_translate][:8]
    if sample_keys:
        sample = {k: {"src": str(src[k]), "tgt": str(tgt[k])} for k in sample_keys}
        context = json.dumps(sample, ensure_ascii=False, indent=1)

    if not apply:
        return True

    translated = translate_map(to_translate, "lang", direction, context)
    for key in removed:
        tgt.pop(key, None)
    for key, value in translated.items():
        tgt[key] = value

    write_lang(tgt_path, tgt, src)
    src_hash_file.write_text(json.dumps(new_hashes), encoding="utf-8")
    print(f"  -> gravado {tgt_path}")
    return True


def sync_reverse_lang(src_path: Path, tgt_path: Path, direction: str, apply: bool) -> bool:
    """Chaves que so existem no zh_cn (escritas a mao) voltam para o en_us."""
    src = load_json(src_path)  # zh_cn
    tgt = load_json(tgt_path)  # en_us
    missing = {k: str(v) for k, v in src.items() if k not in tgt}
    if not missing:
        return False

    print(f"[lang] {src_path}: {len(missing)} chave(s) so no zh_cn -> traduzindo para en_us")
    if not apply:
        return True

    context = ""
    sample_keys = [k for k in src if k not in missing][:8]
    if sample_keys:
        sample = {k: {"src": str(src[k]), "tgt": str(tgt[k])} for k in sample_keys}
        context = json.dumps(sample, ensure_ascii=False, indent=1)

    translated = translate_map(missing, "lang", direction, context)
    tgt.update(translated)
    write_lang(tgt_path, tgt, tgt)
    print(f"  -> gravado {tgt_path}")
    return True


def sync_ptbr_lang(en_path: Path, zh_path: Path, pt_path: Path, apply: bool) -> bool:
    """Etapa 2: traduz en_us -> pt_br usando o zh_cn (ja consensuado) como
    referencia de desambiguacao. Chaves novas/alteradas no en_us sao
    re-traduzidas; chaves apagadas do en_us sao apagadas do pt_br."""
    en = load_json(en_path)
    zh = load_json(zh_path)
    pt = load_json(pt_path)
    if not en:
        return False

    hash_file = en_path.with_suffix(en_path.suffix + f".{PT_BR}.hashes")
    old_hashes: dict = {}
    if hash_file.exists():
        try:
            old_hashes = json.loads(hash_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            old_hashes = {}

    new_hashes = {k: sha1_text(str(v)) for k, v in en.items()}

    to_translate: dict[str, dict[str, str]] = {}
    for key, value in en.items():
        if key not in pt or old_hashes.get(key) != new_hashes[key]:
            to_translate[key] = {"en": str(value), "zh": str(zh.get(key, ""))}

    removed = [k for k in pt if k not in en]
    if not to_translate and not removed:
        return False

    print(f"[lang-pt] {en_path}: {len(to_translate)} para traduzir, {len(removed)} removidas")

    context = ""
    sample_keys = [k for k in en if k not in to_translate][:8]
    if sample_keys:
        sample = {
            k: {"en": str(en[k]), "zh": str(zh.get(k, "")), "pt": str(pt[k])}
            for k in sample_keys
        }
        context = json.dumps(sample, ensure_ascii=False, indent=1)

    if not apply:
        return True

    translated = translate_ptbr_map(to_translate, context)
    for key in removed:
        pt.pop(key, None)
    for key, value in translated.items():
        pt[key] = value

    write_lang(pt_path, pt, en)
    hash_file.write_text(json.dumps(new_hashes), encoding="utf-8")
    print(f"  -> gravado {pt_path}")
    return True


# ---------------------------------------------------------------------------
# Guias (Markdown GuideME)
# ---------------------------------------------------------------------------

FM_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)


def split_front_matter(text: str) -> tuple[dict[str, str], str, str]:
    """Extrai os titulos do front-matter.
    Devolve ({fm_id: linha_title}, head_com_marcadores, corpo)."""
    fm: dict[str, str] = {}
    match = FM_RE.match(text)
    if not match:
        return fm, "", text
    lines = match.group(1).split("\n")
    out_lines: list[str] = []
    counter = 0
    in_navigation = False
    for line in lines:
        stripped = line.strip()
        if re.match(r"^navigation\s*:", line):
            in_navigation = True
            out_lines.append(line)
            continue
        if in_navigation and re.match(r"^title\s*:", stripped):
            fm[f"fm:{counter}"] = stripped
            indent = line[: len(line) - len(line.lstrip())]
            out_lines.append(f"{indent}title: @@FM{counter}@@")
            counter += 1
            continue
        if line and not line.startswith((" ", "\t")):
            in_navigation = False
        out_lines.append(line)
    head = "---\n" + "\n".join(out_lines) + "\n---\n"
    body = text[match.end() :]
    return fm, head, body


def merge_front_matter(head: str, fm: dict[str, str]) -> str:
    for key, title_line in fm.items():
        n = key.split(":")[1]
        head = re.sub(
            rf"^(\s*)title: @@FM{n}@@$",
            lambda m: f"{m.group(1)}{title_line}",
            head,
            count=1,
            flags=re.MULTILINE,
        )
    return head


def split_body_blocks(body: str, limit: int) -> list[tuple[str, bool]]:
    """Divide o corpo em blocos semanticos: paragrafos, tabelas inteiras e
    blocos de tags GuideME (<Row>...</Row>, <GameScene>...</GameScene> etc.)
    nunca sao cortados no meio.
    Devolve [(bloco, era_paragrafo_inteiro)] para remontar as quebras."""
    paragraphs = re.split(r"\n\s*\n", body)
    units: list[tuple[str, bool]] = []
    for para in paragraphs:
        if not para.strip():
            continue
        if len(para) <= limit:
            units.append((para, True))
            continue
        # Bloco grande demais (tabela/lista/tag): quebra por linhas, sem
        # cortar dentro de uma tag GuideME aberta.
        lines = para.split("\n")
        buf = ""
        depth = 0
        for line in lines:
            opens = len(re.findall(r"<[A-Z][A-Za-z]*(?:\s|>|/)", line))
            closes = len(re.findall(r"</[A-Z][A-Za-z]*>", line))
            depth += opens - closes
            buf += line + "\n"
            if depth <= 0 and len(buf) > limit // 2:
                units.append((buf.rstrip("\n"), False))
                buf = ""
                depth = 0
        if buf.strip():
            units.append((buf.rstrip("\n"), False))

    blocks: list[tuple[str, bool]] = []
    buf = ""
    buf_para = True
    for unit, is_para in units:
        if buf and len(buf) + len(unit) + 2 > limit:
            blocks.append((buf, buf_para))
            buf, buf_para = unit, is_para
        else:
            if not buf:
                buf, buf_para = unit, is_para
            else:
                buf = buf + "\n\n" + unit
                buf_para = buf_para and is_para
    if buf.strip():
        blocks.append((buf, buf_para))
    return blocks


def md_needs_translation(src: Path, tgt: Path) -> bool:
    hash_file = tgt.with_suffix(tgt.suffix + ".srchash")
    if not tgt.exists() or not hash_file.exists():
        return True
    current = hashlib.sha1(src.read_bytes()).hexdigest()
    return hash_file.read_text(encoding="utf-8").strip() != current


def translate_markdown_file(src: Path, tgt: Path, direction: str, apply: bool) -> bool:
    if not md_needs_translation(src, tgt):
        return False
    print(f"[guia] {src.relative_to(REPO_ROOT)} -> {tgt.relative_to(REPO_ROOT)}")
    if not apply:
        return True

    text = src.read_text(encoding="utf-8")
    fm, head, body = split_front_matter(text)

    fragments: dict[str, str] = dict(fm)
    blocks = split_body_blocks(body, MD_MAX_CHARS_PER_CALL)
    for i, (block, _) in enumerate(blocks):
        fragments[f"md:{i}"] = block

    translated = translate_map(fragments, "md", direction, "")

    # Remonta o corpo: blocos de paragrafo ganham linha em branco entre si;
    # blocos que foram fatiados de um paragrafo maior sao colados com \n.
    new_body = ""
    for i, (block, _) in enumerate(blocks):
        part = translated.get(f"md:{i}", block)
        if not new_body:
            new_body = part
        elif new_body.endswith("\n") or part.startswith("\n"):
            new_body += part
        else:
            new_body += "\n\n" + part
    if body.startswith("\n") and not new_body.startswith("\n"):
        new_body = "\n" + new_body
    if body.endswith("\n") and not new_body.endswith("\n"):
        new_body += "\n"

    fm_translated = {k: v for k, v in translated.items() if k.startswith("fm:")}
    new_head = merge_front_matter(head, fm_translated)

    tgt.parent.mkdir(parents=True, exist_ok=True)
    tgt.write_text(new_head + new_body, encoding="utf-8")
    tgt.with_suffix(tgt.suffix + ".srchash").write_text(
        hashlib.sha1(src.read_bytes()).hexdigest(), encoding="utf-8"
    )
    print(f"  -> gravado {tgt}")
    return True


def translate_markdown_ptbr_file(src: Path, zh_ref: Path, tgt: Path, apply: bool) -> bool:
    """Etapa 2 para guias: traduz en -> pt_br usando o zh_cn da mesma pagina
    como referencia de desambiguacao."""
    if not md_needs_translation(src, tgt):
        return False
    print(f"[guia-pt] {src.relative_to(REPO_ROOT)} -> {tgt.relative_to(REPO_ROOT)}")
    if not apply:
        return True

    text = src.read_text(encoding="utf-8")
    fm, head, body = split_front_matter(text)

    fragments: dict[str, str] = dict(fm)
    blocks = split_body_blocks(body, MD_MAX_CHARS_PER_CALL)
    for i, (block, _) in enumerate(blocks):
        fragments[f"md:{i}"] = block

    zh_text = ""
    if zh_ref.exists():
        zh_text = zh_ref.read_text(encoding="utf-8")[:MD_REF_MAX_CHARS]

    translated = translate_ptbr_md(fragments, zh_text)

    new_body = ""
    for i, (block, _) in enumerate(blocks):
        part = translated.get(f"md:{i}", block)
        if not new_body:
            new_body = part
        elif new_body.endswith("\n") or part.startswith("\n"):
            new_body += part
        else:
            new_body += "\n\n" + part
    if body.startswith("\n") and not new_body.startswith("\n"):
        new_body = "\n" + new_body
    if body.endswith("\n") and not new_body.endswith("\n"):
        new_body += "\n"

    fm_translated = {k: v for k, v in translated.items() if k.startswith("fm:")}
    new_head = merge_front_matter(head, fm_translated)

    tgt.parent.mkdir(parents=True, exist_ok=True)
    tgt.write_text(new_head + new_body, encoding="utf-8")
    tgt.with_suffix(tgt.suffix + ".srchash").write_text(
        hashlib.sha1(src.read_bytes()).hexdigest(), encoding="utf-8"
    )
    print(f"  -> gravado {tgt}")
    return True


def sync_guides(apply: bool) -> bool:
    changed = False
    guide_root = REPO_ROOT / GUIDE_ROOT
    mirror_root = guide_root / GUIDE_MIRROR_DIR

    # EN -> ZH: arquivos da raiz (fora dos diretorios-espelho)
    for src in sorted(guide_root.rglob("*.md")):
        if any(part in GUIDE_MIRROR_DIRS for part in src.relative_to(guide_root).parts):
            continue
        rel = src.relative_to(guide_root)
        tgt = mirror_root / rel
        changed |= translate_markdown_file(
            src, tgt, "Translate each fragment from English to Simplified Chinese.", apply
        )

    # ZH -> EN: arquivos que so existem no espelho (escritos a mao em chines)
    if mirror_root.exists():
        for src in sorted(mirror_root.rglob("*.md")):
            rel = src.relative_to(mirror_root)
            tgt = guide_root / rel
            if tgt.exists():
                continue
            changed |= translate_markdown_file(
                src, tgt, "Translate each fragment from Simplified Chinese to English.", apply
            )

    # Remover espelhos cuja fonte em ingles foi apagada
    if mirror_root.exists():
        for tgt in sorted(mirror_root.rglob("*.md")):
            rel = tgt.relative_to(mirror_root)
            if not (guide_root / rel).exists():
                print(f"[guia] fonte removida, apagando espelho {tgt.relative_to(REPO_ROOT)}")
                if apply:
                    tgt.unlink()
                    hash_file = tgt.with_suffix(tgt.suffix + ".srchash")
                    if hash_file.exists():
                        hash_file.unlink()
                changed = True
    return changed


def sync_ptbr_guides(apply: bool) -> bool:
    """Etapa 2 para guias: gera _pt_br/ a partir do ingles, usando o _zh_cn/
    ja consensuado como referencia de desambiguacao."""
    changed = False
    guide_root = REPO_ROOT / GUIDE_ROOT
    zh_root = guide_root / GUIDE_MIRROR_DIR
    pt_root = guide_root / PTBR_GUIDE_MIRROR_DIR

    for src in sorted(guide_root.rglob("*.md")):
        if any(part in GUIDE_MIRROR_DIRS for part in src.relative_to(guide_root).parts):
            continue
        rel = src.relative_to(guide_root)
        tgt = pt_root / rel
        zh_ref = zh_root / rel
        changed |= translate_markdown_ptbr_file(src, zh_ref, tgt, apply)

    # Remover espelhos pt_br cuja fonte em ingles foi apagada
    if pt_root.exists():
        for tgt in sorted(pt_root.rglob("*.md")):
            rel = tgt.relative_to(pt_root)
            if not (guide_root / rel).exists():
                print(f"[guia-pt] fonte removida, apagando espelho {tgt.relative_to(REPO_ROOT)}")
                if apply:
                    tgt.unlink()
                    hash_file = tgt.with_suffix(tgt.suffix + ".srchash")
                    if hash_file.exists():
                        hash_file.unlink()
                changed = True
    return changed


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="so detecta pendencias, nao traduz")
    args = parser.parse_args()
    apply = not args.check

    changed = False

    # Etapa 1: sincroniza en_us <-> zh_cn (consenso contextual)
    for lang_dir in LANG_DIRS:
        for src_name, tgt_name in LANG_PAIRS:
            base = REPO_ROOT / lang_dir
            src_path = base / f"{src_name}.json"
            tgt_path = base / f"{tgt_name}.json"
            if not src_path.exists():
                continue
            direction = (
                f"Translate each value from {src_name} (English) to {tgt_name} (Simplified Chinese)."
                if tgt_name == "zh_cn"
                else f"Translate each value from {src_name} to {tgt_name}."
            )
            changed |= sync_lang_file(src_path, tgt_path, direction, apply)
            if tgt_path.exists():
                changed |= sync_reverse_lang(
                    tgt_path,
                    src_path,
                    "Translate each value from Simplified Chinese to English (game string).",
                    apply,
                )

    changed |= sync_guides(apply)

    # Etapa 2: usa o consenso en_us <-> zh_cn para traduzir para pt_br
    for lang_dir in LANG_DIRS:
        base = REPO_ROOT / lang_dir
        en_path = base / "en_us.json"
        zh_path = base / "zh_cn.json"
        pt_path = base / f"{PT_BR}.json"
        if en_path.exists() and zh_path.exists():
            changed |= sync_ptbr_lang(en_path, zh_path, pt_path, apply)

    changed |= sync_ptbr_guides(apply)

    if not changed:
        print("Nenhuma alteracao de idioma pendente.")
    elif not apply:
        print("Alteracoes de idioma detectadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
