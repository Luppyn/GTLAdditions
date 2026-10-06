---
navigation:
  title: 时空扭曲器
  icon: time_space_distorter
  parent: controller/multiblock_controller.md
  position: 10
item_ids:
  - time_space_distorter
---

# 时空扭曲器

<BlockImage id = "time_space_distorter" scale = "8"/>

> 能耗倍率：0.1 \
> 包含[多配方类型](../multi_type.md)：量子操纵器、深度化学扭曲 \
> 运行**深度化学扭曲配方**时，并行数计算方式为：机器并行数 / 配方需求温度^0.8 \
> 配方概率输入的几率变为原来的十分之一。配方概率输入的Tier Chance全部变为0。若概率消耗物品为**纳米蜂群**，则变为**不消耗** \
> 机器成型后，可打开GUI调整增幅次数倍率 \
> **增幅次数1**：额外消耗配方并行数 / 70mb的<FluidLink id="gtceu:infinity" />，配方输出概率变为100% \
> **增幅次数2**：在增幅次数1的基础上，额外消耗配方并行数 / 180mb的<FluidLink id="gtceu:hypogen" />，配方输出变为1.5倍 \
> **增幅次数3**：在增幅次数2的基础上，额外消耗配方并行数 / 340mb的<FluidLink id="gtceu:spacetime" />，配方输出变为3倍 \
> GUI可选择是否启用均分模式 \
> 在非均分模式下，超频模式变为6倍功率2倍速度 \
> 均分模式**不受**增幅次数调整影响 \
> 启用后，每处理一个配方需要消耗配方并行数 / 108的<ItemLink id="kubejs:quantum_anomaly" />以及配方并行数 / 623的<ItemLink id="kubejs:hypercube" /> \
> 配方输出概率变为100%，超频模式变为完美超频 \
> 由于奇迹的固有不可预测性，以下配方概率无法修改

<Recipe id="gtceu:qft/make_miracle_crystal" />
