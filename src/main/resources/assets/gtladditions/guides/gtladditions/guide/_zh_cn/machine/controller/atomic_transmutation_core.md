---
navigation:
  title: 原子转化核心
  icon: atomic_transmutation_core
  parent: controller/multiblock_controller.md
  position: 10
item_ids:
  - atomic_transmutation_core
---

# 原子转化核心

<BlockImage id = "atomic_transmutation_core" scale = "8"/>

* 需要安装 <ItemLink id="gtladditions:me_block_conservation" /> 才能使用
* 可在机器 GUI 中插入（快速或终极）转化卡
* 机器成型后将持续空转 ~~（不是 bug 而是特性）~~，每个工作周期后转化**转化总线**中的方块
* 能耗对应机器当前电压等级的电功率
* 每次操作的方块转化数量等于并行数
* 使用终极转化卡时，可一次转化多个方块，工作时间缩短至 1 秒

> 转化卡提供 `e^电压等级` 并行 \
> 快速转化卡提供 `4^电压等级` 并行 \
> 终极转化卡提供 `5.7^电压等级` 并行

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
