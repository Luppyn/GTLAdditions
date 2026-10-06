---
navigation:
  title: 太虚浊化阵列
  icon: taixu_turbid_array
  parent: controller/multiblock_controller.md
  position: 10
item_ids:
  - taixu_turbid_array
---

# 太虚浊化阵列

<BlockImage id = "taixu_turbid_array" scale = "8"/>

> 你可以打开主控制器的 GUI，并在 GUI 右下角的物品槽中放入对应的纳米蜂群或创造能量仓 \
> 当放入**创造能量仓**时，放入一个即可获得 3^16 并行数与 100% 成功率加成（~~放入多个效果相同~~） \
> 当放入对应的纳米蜂群时，你会获得额外的成功率加成，加成值为放入的纳米蜂群数量 × 基础加成 \
> 最多可放入 64 个纳米蜂群或创造能量仓 \
> 当放入**末影纳米蜂群**时，基础加成为 0.01 \
> 当放入**龙纳米蜂群**时，基础加成为 0.05 \
> 当放入**时空纳米蜂群**时，基础加成为 0.1 \
> 当放入**永恒纳米蜂群**时，基础加成为 0.2

* 该机器结构只能有一个激光仓
* 当机器电压等级大于或等于 <Color color="#FFFF00">**UXV**</Color> 时，解锁 **UU 增幅器**输出
* 当机器电压等级大于或等于 <Color color="#FF0000">**MAX**</Color> 时，解锁 **UU 物质**输出
* ~~当机器电压等级未达到时，将不会有额外的 UU 增幅器或 UU 物质输出~~
* 机器的固定能耗为其当前电压等级对应功率的 524,288 倍；默认运行时间为 5 秒，放入能量创造室时缩短至 1 秒。

> **~~大量公式警告~~**

* 每级恒星热容器的加成 α 计算公式：
> <Latex math = "\alpha = 8 * (2^{Stellar Containment Tier} - 1) * \sqrt{Voltage Tier + 1}" />

* 每级线圈的加成 β 计算公式：
> <Latex math = "\beta = 3.8 * 1.3^{Coil Level} * (\frac{Coil Temperature}{36000})^{0.7}" />

* UU 增幅器成功概率计算公式：
> <Latex math = "1/(1 + e^{-0.1 * (\frac{\alpha}{50} + \frac{\beta}{100} + \frac{height}{3})})" />

* UU 增幅器基础输出计算公式：
> <Latex math = "40960 * \tanh{(0.007 * (\alpha * \frac{height}{9} + \sqrt{\beta} * \ln{(Voltage Tier + 2)}))}" />

* UU 物质成功概率计算公式：
> <Latex math = "1/(1 - e^{-0.02 * (\frac{\alpha + \beta}{20} + \sqrt[3]{height} * \frac{Voltage Tier}{3})})" />

* UU 物质基础输出计算公式：
> <Latex math = "22500 * \tanh{(\sqrt{\alpha * \beta} * \frac{(height + Voltage Tier) * 0.045}{200})}" />

* 机器并行计算公式：
> <Latex math = "4096 * 1.621^{\min(\frac{Coil Temperature}{6400},12)}" />

* **注意**：公式中的高度指的是结构中重复层的高度，类似于蒸馏塔或中子活化器的高度
