[English](README.en.md)
[简体中文](README.zh.md)

<div align="center">
# GTLAdditions
</div>

> **[!TIP]**
> GTLAdditions é um mod que adiciona novas receitas e máquinas ao `GregTech Leisure`
> Você pode carregá-lo no seu GTL com o core **mais recente**!
> ***Siga o contrato de licença se você não quiser se tornar um babaca***

## Introdução

Este mod foi desenvolvido com base no `GregTech Leisure`. Sobre a base deste Modpack, muitas ideias novas foram adicionadas. Mantendo a estrutura original de tecnologia hardcore, ele incorpora uma grande quantidade de designs inovadores e otimizações balanceadas, com o objetivo de trazer aos jogadores uma experiência de automação mais fluida e estratégica.

## Requisitos

- GTLCore `Versão >= 1.2.3.2-fix2`
- Kotlin For Forge `Versão >= 4.11.0`
- Java `Versão >= 21`

## Instalação

Primeiro, baixe o `GregTech Leisure` [aqui](https://pan.quark.cn/s/d13f899cdab5#/list/share) ou [aqui](https://drive.google.com/drive/folders/1Ga_w-TmDKNru0me1kAM_gXyedz_Ne4-x), e instale-o com o seu launcher do Minecraft

Depois, delete o `GTLCore` e instale o mais recente; você pode encontrá-lo [aqui](https://github.com/AaAdoniSsS/GTLCore)

Por fim, adicione este mod à pasta `/mods`

Aproveite sua experiência com o GregTech Leisure! ~~talvez você veja essas máquinas depois que não quiser mais jogar GregTech Leisure~~

## Parâmetros de JVM recomendados

> -Xms4G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:+PerfDisableSharedMem -XX:G1HeapWastePercent=8 -XX:G1MixedGCCountTarget=6 -XX:G1ReservePercent=10 \
> -XX:+UseCompactObjectHeaders (se você usar Java25)

## Funcionalidades

### Máquinas Multibloco

Este mod adicionou muitas máquinas melhores para substituir as máquinas originais

| Máquinas                                    | Receitas                                                                                            | Utilização                                                                                                                                                                                                                                                           |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Floating Light Deep Space Industrial Vessel | executa receitas de `plants`                                                                        | Geral                                                                                                                                                                                                                                                                |
| Atomic Transmutation Core                   | Transmutation Block Conversion                                                                      | Funciona como `Block Conversion Room`, mas com mais eficiência                                                                                                                                                                                                       |
| Lucid Etchdreamer                           | Photon Matrix Etch                                                                                  | Funciona como `Dimensional Focus Engraving Array`, mas sem usar `Photoresist`, `Computation Power` e `Research Data`                                                                                                                                                 |
| Astral Convergence Nexus                    | Space Assembler Module                                                                              | Funciona como `Space Assembler Module`                                                                                                                                                                                                                               |
| Nebula Reaper                               | Space Miner Module *e* Space Drilling Module                                                        | Funciona como `Space Miner Module` *e* `Space Drilling Module`, mas usa lógica de múltiplas receitas                                                                                                                                                                 |
| Arcanic Astrograph                          | Cosmos Simulation                                                                                   | Funciona como `Eye of Harmony`, mas com mais eficiência                                                                                                                                                                                                              |
| Arcane Cache Vault                          | Packer                                                                                              | Funciona como `Packer`, mas usa lógica de múltiplas receitas                                                                                                                                                                                                         |
| Draconic Collapse Core                      | Aggregation Device                                                                                  | Funciona como `Aggregation Device` com mais paralelismo, podendo usar HugeInputHatch e ME Pattern Buffer                                                                                                                                                             |
| Titan Crip Earthbore                        | Tectonic Fault Generater                                                                            | Produz `Bedrock dust`                                                                                                                                                                                                                                                |
| Biological Simulation Laboratoy             | Biological Simulation                                                                               | Produz recursos a partir de entidades com `world data`, `swords` e `spawn egg`                                                                                                                                                                                       |
| Dimensionally Transcendent Chemical Plant   | Large Chemical Reactor                                                                              | Funciona como `Large Chemical Reactor`, mas usa lógica de múltiplas receitas                                                                                                                                                                                         |
| Quantum Syphon Martix                       | Voidflux Reaction                                                                                   | Produz a série `Air`                                                                                                                                                                                                                                                 |
| Fuxi Bagua Heaven Forging Furnace           | Stellar Lgintion *e* Chaotic Alchemy *e* Molecular Deconstruction *e* Ultimate Material Forge       | Stellar Lgintion pode transmutar alguns tipos de `Gas` ou `Liquid` em `Plasma`, Chaotic Alchemy funciona como `Alloy Blast Smelter`, mas produz `Liquid`, Molecular Deconstruction pode extrair alguns `dust` (que originalmente não podiam ser extraídos diretamente) em `Liquid` |
| Antientropy Condensation Center             | Antientropy Condensation                                                                            | Funciona como `Cooling Tower`, mas sem usar `Liquid Helium`                                                                                                                                                                                                          |
| Taixu Turbid Array                          | Chaos Weave                                                                                         | Produz `Scrap Box`, `UU Amplifier` *e* `UU Matter`                                                                                                                                                                                                                   |
| Inferno Cleft Smelting Vault                | Pyrolyse Oven *e* Cracker                                                                           | Funciona como `Large Pyrolyse Oven` *e* `Large Recycler` e usa lógica de múltiplas receitas                                                                                                                                                                          |
| Skeleton Shift Rift Engine                  | Decay Hastener, Fusion Reactor *e* Particle Collision                                               | Funciona como `Decay Hastener`, `Fusion Reactor` *e* `Super Particle Collider`, mas com mais eficiência                                                                                                                                                              |
| Recursive Reverse Forge                     | Dimensionally Transcendent Smelting e Stellar Thermal Smelting                                     | Funciona como `Dimensionally Transcendent Plasma Forge`, mas com mais eficiência                                                                                                                                                                                     |
| Time Space Distorter                        | Quantum Manipulator e Deep Chemical Distortion                                                     | Funciona como `Quantum Field Transformer` e `Deep Chemical Distorter`, mas com mais eficiência                                                                                                                                                                       |
| Planetary Ionisation Convergence Tower      | null                                                                                                | Opções alternativas para geração de energia em UHV e além                                                                                                                                                                                                            |
| Primordial Evolution Nexus                  | Evolution Of Primordial                                                                             | Funciona como `Wood Distillation Plant` e `Petrochemical Plant`, mas com mais eficiência                                                                                                                                                                             |
| Biosphere III                               | Greenhouse e Fishground                                                                             | Funciona como `Large Greenhouse` e `Fish Ground`, mas usa lógica de múltiplas receitas                                                                                                                                                                               |
| Space Elevator MKII                         | Space Elevator                                                                                      | Funciona como `Space Elevator`, mas tem mais slots disponíveis para módulos                                                                                                                                                                                          |

- Os limites superiores de entrada de `Gaseous Hydrogen` e `Gaseous Helium` para o `Eye of Harmony` foram restringidos a 10.000.000.000 mB

### Partes de Máquina Multibloco

| Hatch                                             | Geral                                                                                                                        |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Laser Hatch                                       | Um Laser Hatch maior que a versão original. A amperagem é `16777216A` *e* `67108863A`                                        |
| Wireless Laser Hatch                              | Semelhante ao `Laser Hatch`, mas não requer fiação                                                                            |
| Huge Output Dual Hatch                            | Semelhante ao `Huge Input Dual Hatch`, mas com maior capacidade                                                               |
| Huge Steam Input Hatch                            | Como o Large Steam Input Hatch. Eleva a restrição de receita da multibloco a vapor para **HV** *e* a duração passa a ser **1t** |
| Super Input Dual Hatch                            | Semelhante ao `Huge Input Dual Hatch`, mas com mais espaço de entrada                                                          |
| Spectral Analysis Hatch                           | Enhanced Integrated Ore Processor e Advanced Integrated Ore Processor                                                        |
| Transmutation Bus Hatch                           | Usado no Atomic Transmutation Core, Door of Creation e Creative Aggregator                                                    |
| Ventiane Transcription Node                       | Emite sinal de redstone para o Catalytic Cascade Array e o Reverse Time Boosting Engine                                       |
| Cloud Computation / Research Data Hatch / Machine | Sistemas mais avançados de computação / dados de pesquisa                                                                     |

Além disso, também existem algumas Partes profanadas

- `WirelessOpticalDataHatch` *e* `WirelessOpticalComputationHatch` permitem o **compartilhamento** de Máquinas Multibloco
- A série `AutoConfigurationMaintenanceHatch` também permite o **compartilhamento** de Máquinas Multibloco *e* há um slot onde itens diferentes podem ser colocados para obter bônus diferentes

### Receitas

- Muitas receitas simplificadas foram adicionadas, o que pode ajudar a otimizar linhas de produção em larga escala. Aprenda a usar o **`jei`** para encontrar receitas. Se uma receita for adicionada pelo `GTLAdditions`, haverá uma dica explicando (então você pode consultar o jei frequentemente no seu dia a dia. Você sempre encontrará receitas novas)
- A adição de chips e wafers SOC totalmente novos possibilita uma produção de circuitos mais eficiente

Para mais informações, consulte o guia do GTLAdditions dentro do jogo.
