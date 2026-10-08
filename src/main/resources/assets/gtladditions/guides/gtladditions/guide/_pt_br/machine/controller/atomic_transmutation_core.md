---
navigation:
  title: Núcleo de Transmutação Atômica
  icon: atomic_transmutation_core
  parent: controller/multiblock_controller.md
  position: 10
item_ids:
  - atomic_transmutation_core
---

# Núcleo de Transmutação Atômica

<BlockImage id = "atomic_transmutation_core" scale = "8"/>

* Requer <ItemLink id="gtladditions:me_block_conservation" /> instalado para ser usado
* Pode inserir cartões de Conversão (Rápido ou Supremo) na GUI da máquina
* A máquina ficará em espera continuamente após ser formada ~~(não é um bug, é uma funcionalidade)~~, convertendo blocos no **barramento de transmutação** após cada ciclo de trabalho
* O consumo de energia corresponde à potência do nível de voltagem atual da máquina
* O número de blocos convertidos por operação é igual à contagem de paralelos
* Ao usar o cartão de conversão Supremo, pode converter vários blocos de uma vez, com o tempo de trabalho reduzido para 1 segundo

> O cartão de Conversão fornece `e^nível de voltagem` de paralelos \
> O cartão de Conversão Rápido fornece `4^nível de voltagem` de paralelos \
> O cartão de Conversão Supremo fornece `5.7^nível de voltagem` de paralelos

<Row>
    <Recipe id="gtladditions:transmutation_block_conversion/block.kubejs.draconium_block_charged" />

    <Recipe id="gtladditions:transmutation_block_conversion/block.minecraft.moss_block" />

    <Recipe id="gtladditions:transmutation_block_conversion/block.minecraft.warped_stem" />

    <Recipe id="gtladditions:transmutation_block_conversion/block.minecraft.sculk" />
</Row>

<Row>
    <Recipe id="gtladditions:transmutation_block_conversion/block.minecraft.crimson_stem" />

    <Recipe id="gtladditions:transmutation_block_conversion/block.minecraft.bone_block" />

    <Recipe id="gtladditions:transmutation_block_conversion/block.kubejs.essence_block" />
</Row>
