---
navigation:
  title: 反熵凝聚
  icon: antientropy_condensation_center
  parent: controller/multiblock_controller.md
  position: 10
item_ids:
  - antientropy_condensation_center
---

# 反熵凝聚

<BlockImage id = "antientropy_condensation_center" scale = "4"/>

* 该机器在每次运行前会消耗冰晶尘。消耗量由以下公式计算：

> <Latex math = "Cryotheum Dust Consumption = \frac{5 * (\frac{Recipe Parallel}{2^{19}} + 51 * \ln{Recipe Parallel})}{Voltage Tier - 9}" />

* 你可以手持 <ItemLink id="kubejs:create_ultimate_battery" /> 并右键点击，将其插入机器以获得如下额外加成：
* 时间倍率：0.7；能量倍率：0.5
* **注意**：若机器被拆除，加成效果将会重置，且创造终极电池不会返还
