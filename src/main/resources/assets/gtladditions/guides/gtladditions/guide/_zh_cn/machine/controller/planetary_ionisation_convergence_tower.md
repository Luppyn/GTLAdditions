---
navigation:
  title: 行星电离汇聚塔
  icon: planetary_ionisation_convergence_tower
  parent: controller/multiblock_controller.md
  position: 10
item_ids:
  - planetary_ionisation_convergence_tower
---

# 行星电离汇聚塔

<BlockImage id = "planetary_ionisation_convergence_tower" scale = "8"/>

* 只能使用钛级或更高级别的线圈；
* 运行周期持续 3 秒；
* 如果内部能量缓冲已满时仍有能量持续输入，将以机器为中心发生半径 100 格的爆炸，并在无线电网中消散相当于线圈瞬时脉冲能量 1,024 倍的能量；
* 在运行周期开始时，一个_瞬时_、极高功率的 EU 脉冲（1 tick）被注入内部能量缓冲，随后在周期剩余时间内以较低功率平稳_放电_进入缓冲；
* 脉冲结束后，内部能量缓冲将通过能量仓/激光源仓向外部环境输出能量：
* 恒星热力学容器的等级影响内部能量缓冲容量：
> 基础：890,000,000,000,000 EU \
> 进阶：132,000,000,000,000,000 EU\
> 终极：1,570,000,000,000,000,000 EU
* 线圈等级影响所消耗流体的类型、每周期消耗速率以及发电量
> 钛钢至精金：<FluidLink id="gtceu:rhenium" /> 73,728 mB，<FluidLink id="gtceu:ice" /> 8 KB，<ItemLink id="kubejs:space_drone_mk2" /> 2×10⁻⁴ 单位 \
> 钠克夸德里亚钛至星金：<FluidLink id="gtceu:promethium" /> 36,864 MB，<FluidLink id="gtceu:liquid_helium" /> 4 KB，<ItemLink id="kubejs:space_drone_mk4" /> 1×10⁻⁴ 单位 \
> 无尽至永恒：<FluidLink id="gtceu:crystalmatrix" /> 9216 MB，<FluidLink id="kubejs:gelid_cryotheum" /> 1 KB，<ItemLink id="kubejs:space_drone_mk6" /> 2.5×10⁻⁵ 单位 \
>
> | 线圈等级             | 瞬时（A MAX）  | 放电（A MAX）  |
> |-----------------------|-----------------------|-------------------|
> | 钛钢           | 4,096                 | 16                |
> | 精金            | 32,768                | 128               |
> | 钠克夸德里亚钛 | 524,288               | 256               |
> | 星金            | 4,194,304             | 2,048             |
> | 无尽              | 8,388,608             | 4,096             |
> | 氢源               | 67,108,864            | 32,768            |
> | 永恒              | 268,435,456           | 131,072           |
* 手持 <ItemLink id="gtmthings:creative_laser_hatch"/> 右键点击以将其插入机器，激活特殊超频模式：
> 运行周期缩短至 1 秒；所有能量直接输出到无线电网，且无论线圈等级和内部缓冲如何，最大单次输出电流提升至 64A MAX+16
* 此时的材料消耗和类型为：
> <FluidLink id="gtceu:miracle" /> 10mB，<ItemLink id="kubejs:hyperdimensional_drone" /> 1x10^(-6) 单位
* **注意**：如果主机被移除，特殊超频模式将被重置，且创造激光仓不会返还。