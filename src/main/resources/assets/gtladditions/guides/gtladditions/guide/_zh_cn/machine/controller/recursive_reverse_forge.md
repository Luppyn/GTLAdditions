---
navigation:
  title: 递归逆锻炉
  icon: recursive_reverse_forge
  parent: controller/multiblock_controller.md
  position: 10
item_ids:
  - recursive_reverse_forge
  - reverse_time_boosting_engine
  - catalytic_cascade_array
  - magnetorheological_convergence_core
  - hyperdimensional_energy_concentrator
  - fractal_manipulator
---

# 递归逆锻炉

<BlockImage id = "recursive_reverse_forge" scale = "8"/>

* 能耗系数：0.8
* 最大并行数：2,147,483,647
* 拥有[多方块配方类型](../multi_type.md)：维度超越等离子锻炉、恒星锻炉
* 完美超频，且超频次数无限
* 仅可使用激光仓
* 可安装模块以获得额外加成

### 逆时增幅引擎

<BlockImage id = "reverse_time_boosting_engine" scale = "4"/>

* **仅可安装在递归逆锻炉的结构上，且每台递归逆锻炉只能安装一个此模块**

> 安装模块后，配方时间可缩短的倍数为： \
> <Latex math = "\min{(0.8, 0.05+0.8*e^{-3.2*input ratio^{1.9}})}" /> \
> 输入比例为：输入数量乘以 2/(初始配方输出数量 * 当前温度)，输入比例不会大于 1，且当输入比例小于 10% 时时间缩短函数不会生效（初始配方输出数量指在 1 并行且无额外加成下运行一次配方的输出）\
> 只需输入一种输出物品或流体。不要使用 <FluidLink id="gtceu:dimensionallytranscendentresidue" />、<ItemLink id="kubejs:extremely_durable_plasma_cell" />、<ItemLink id="kubejs:time_dilation_containment_unit" />、<ItemLink id="kubejs:plasma_containment_cell" /> \
> 初始温度为 48000K，若机器处于工作状态，温度将以 65K/t 的速度升高，处于非工作状态时，温度将以 900K/s 的速度降低（不低于 48000K） \
> 可通入不同流体来控制温度。加热介质可为 <FluidLink id="minecraft:lava" />2500K、<FluidLink id="gtceu:blaze" />4600K、<FluidLink id="gtceu:raw_star_matter" />14000K，冷却流体可为 <FluidLink id="gtceu:ice" />1900K、<FluidLink id="gtceu:helium" />3400K、<FluidLink id="kubejs:gelid_cryotheum" />6700K \
> 加热介质与冷却液的消耗速率均为 100B/1s \
> 输入的配方产物将在配方处理完成后按比例返还 \
> 当温度处于 [93000K, 97000K] 范围内时，返还比例为 100% \
> 当温度低于该范围下限时，返还比例为：  \
> <Latex math = "0.5+0.5*\frac{current temperature-48000}{45000}" /> \
> 当温度超过该范围上限时，返还比例为： \
> <Latex math = "1-0.85*(\frac{current temperature-97000}{13000})^{0.42}" /> \
> 当温度超过 105000K 时将触发过热保护机制。默认情况下，温度以 7125K/s 的冷却速率降低（使用冷却液可额外提高冷却速率；实际冷却速率为默认速率加上冷却液冷却速率）。所连接的递归逆锻炉在降至 48000K 之前将不会处理配方 \
> 可安装 <ItemLink id="gtladditions:vientiane_transcription_node" /> 来控制温度，类似于中子传感器 \
> **仅**可使用巨型输入总线来提供温控流体。**仅**可使用 <ItemLink id="super_input_dual_hatch" /> 为配方产物提供输入

### 催化级联阵列

<BlockImage id = "catalytic_cascade_array" scale = "4"/>

* **仅可安装在递归逆锻炉的结构上，且每台递归逆锻炉只能安装一个此模块**

> 安装此模块后，配方的能耗可乘以 0.15，且配方的输出可翻倍 \
> 它具有 30 秒的催化剂**循环周期**。在每个催化剂循环开始时，模块将随机输出 1 到 15 的红石信号 \
> 输出的红石信号需要通过 <ItemLink id="gtladditions:vientiane_transcription_node" /> 接收 \
> **仅**可使用 LV 巨型输入仓来接收输入的催化剂 \
> 若红石信号为 1 到 3，则表示本周期使用的催化剂为 <FluidLink id="gtceu:dimensionallytranscendentcrudecatalyst" />。按此规律，后续顺序为 <FluidLink id="gtceu:dimensionallytranscendentprosaiccatalyst" />、
> <FluidLink id="gtceu:dimensionallytranscendentresplendentcatalyst" />、<FluidLink id="gtceu:dimensionallytranscendentexoticcatalyst" /> 和 <FluidLink id="gtceu:dimensionallytranscendentstellarcatalyst" /> \
> 在循环的前 0 到 5 秒内，模块不会生效。5 秒后，模块将根据输出的红石信号消耗催化剂。催化剂消耗速率为 40B/s，效果将持续到下一循环的第五秒 \
> 若输入了错误的催化剂，则本循环剩余时间内不会增产，且后续输入的任何催化剂都会被消耗，但能耗降低效果仍会保留 \
> 当前及后续处理含有 <ItemLink id="kubejs:extremely_durable_plasma_cell" />、<ItemLink id="kubejs:time_dilation_containment_unit" /> 和 <ItemLink id="kubejs:plasma_containment_cell" /> 的配方将不纳入翻倍过程 \
> **磁流变汇聚核心模块的优先级高于此模块**

### 磁流变汇聚核心

<BlockImage id = "magnetorheological_convergence_core" scale = "4"/>

* **仅可安装在递归逆锻炉的结构上，且每台递归逆锻炉只能安装一个此模块**

> 安装此模块后，配方输出可聚焦于第一种物品和流体，将第二种产物的输出转化为第一种产物的额外输出 \
> 它具有 12 秒的燃料输入周期，且**仅**可使用两个 ULV 巨型输入总线和一个 LV 巨型输入仓来接收燃料 \
> 当模块首次激活时，它将从 <ItemLink id="kubejs:black_body_naquadria_supersolid" />、<ItemLink id="kubejs:quantum_anomaly" />、<ItemLink id="kubejs:hyper_stable_self_healing_adhesive" />、<FluidLink id="gtceu:exciteddtec" /> 和 <FluidLink id="gtceu:exciteddtsc" /> 中随机选择两种物品和一种流体作为维持模块运行的燃料 \
> 模块选定的正确燃料需要精确输入才能激活聚焦功能。若输入数量不正确，模块的 GUI 中将显示错误信息 \
> 同时，固定消耗 2/s 的熔融物质块。若输入不足，则配方无法聚焦且无法输出 \
> 当前及后续处理含有 <ItemLink id="kubejs:extremely_durable_plasma_cell" />、<ItemLink id="kubejs:time_dilation_containment_unit" /> 和 <ItemLink id="kubejs:plasma_containment_cell" /> 的配方将不纳入翻倍过程 \
> **逆时增幅引擎模块的优先级高于此模块**

### 超维能量汇聚器

<BlockImage id = "hyperdimensional_energy_concentrator" scale = "4"/>

* **仅可安装在递归逆锻炉的结构上，且每台递归逆锻炉只能安装一个此模块**

> 安装模块后，递归逆锻炉可直接从无线能量网络获取能量来工作 \
> 应将 <ItemLink id="kubejs:hyperdimensional_drone" /> 放入主模块中。每放入一个，可获取的最大能量将增加 16A 
> <Color color="#FF0000">**M**</Color><Color color="#00FF00">**A**</Color><Color color="#0000FF">**X**</Color><Color color="#FFFF00">**+**</Color><Color color="#FF0000">**16**</Color> \
> 基础可获取的最大功率为 1A MAX，需要放入超维无人机来提高功率上限（这也会将配方等级锁定为 MAX），最多可放入 64 个 \
> 每小时会发射（消耗）一个超维无人机，以维持与无线能量网络的连接 \
> 需要提供 524,288 CWU/t、64A <Color color="#FF0000">**MAX**</Color> 和 240B/s 的极寒冰晶来维持模块运行

### 分形操纵器

<BlockImage id = "fractal_manipulator" scale = "4"/>

* **仅可安装在递归逆锻炉结构上，且每台递归逆锻炉最多只能容纳四个此模块**

> 能耗系数：0.8 \
> 最大并行数：2,147,483,647 \
> 完美超频，且超频次数无限 \
> 仅可使用激光仓 \
> 它可与递归逆锻炉共享催化级联阵列和超维能量汇聚器 \
> 此模块**当且仅当**逆时增幅引擎模块完美运行时才会工作 \
> 每次运行需要消耗一个促进剂，不参与并行计算，并在配方完成后返还
