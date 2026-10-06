---
navigation:
  title: 关于创造之门与创造聚合器的修改
  parent: modify/modify_index.md
  position: 7
item_ids:
  - gtceu:door_of_create
  - gtceu:create_aggregation
---

# 关于创造之门与创造聚合器的修改

<Row>
    <BlockImage id = "gtceu:door_of_create" scale = "4" />

    <BlockImage id = "gtceu:create_aggregation" scale = "4" />
</Row>

* 可通过安装 <ItemLink id="gtladditions:me_block_conservation" /> 进行转换
* 在输入总线中选择电路 24 以运行转换
* 机器中只能放置 **终极转换卡**，它提供并行加成。没有它机器将无法工作
* 创造之门：65536 并行；创造聚合器：8192 并行
* 手持 <ItemLink id="gtceu:creative_data_access_hatch" /> 并右键点击 **嬗变总线** 进行安装以正常运行
* **嬗变总线** 的其他使用方法与 <ItemLink id="gtladditions:atomic_transmutation_core" /> 类似
* 在输入总线中选择电路 1 以进入原版模式

### 创造之门配方
<Row>
    <Recipe id="gtladditions:transmutation_block_conversion/tagprefix.block" />

    <Recipe id="gtladditions:transmutation_block_conversion/block.minecraft.command_block" />
</Row>

### 创造聚合器配方
<Row>
    <Recipe id="gtladditions:transmutation_block_conversion/block.minecraft.chain_command_block" />

    <Recipe id="gtladditions:transmutation_block_conversion/block.minecraft.repeating_command_block" />
</Row>
