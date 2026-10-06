---
navigation:
  title: 云算力/研究数据系统
  icon: gtmthings:iv_huge_output_dual_hatch
  parent: part/machine_part_index.md
  position: 10
item_ids:
  - gtladditions:cloud_data_hatch
  - gtladditions:cloud_data_machine
  - gtladditions:cloud_computation_monitor
  - gtladditions:cloud_computation_transmitter_hatch
  - gtladditions:cloud_computation_receiver_hatch
  - gtceu:research_station
---

# 云算力/研究数据系统

<Row>
    <BlockImage id="gtladditions:cloud_data_hatch" scale="3" />

    <BlockImage id="gtladditions:cloud_data_machine" scale="3" />

    <BlockImage id="gtladditions:cloud_computation_monitor" scale="3" />

    <BlockImage id="gtladditions:cloud_computation_transmitter_hatch" scale="3" />

    <BlockImage id="gtladditions:cloud_computation_receiver_hatch" scale="3" />
</Row>

* 你可以在 <Color color="#55FF55">**UEV**</Color> 阶段制作它
* 云算力发射仓相当于 <ItemLink id="gtmthings:wireless_computation_transmitter_hatch" />，而算力接收仓相当于 <ItemLink id="gtmthings:wireless_computation_receiver_hatch" />；云算力监控器负责监控云算力系统的算力输入/输出状态
* 只有具备桥接能力的多方块结构才能为云算力系统提供算力；一旦云算力监控器高亮了坐标，如果机器与玩家处于同一维度，GUI 将会关闭并将玩家的视角转向该机器；如果处于不同维度，聊天栏将显示坐标，玩家可以传送过去
* <ItemLink id="gtceu:network_switch" /> *无法放置* 云算力发射/接收仓
* 云研究数据仓相当于 <ItemLink id="gtceu:wireless_data_receiver_hatch" />
* 云研究数据机负责在云研究数据系统中存储数据模块、数据球和闪存；每个数据模块、数据球或闪存单元都会增加 393,216 EU/t 的能耗。当放置在创造模式数据访问仓内时，它会向所有数据仓提供全部研究数据，并且锁定能耗为 393,216 EU/t（机器被破坏时，创造模式数据访问仓*不会*掉落）
* 一旦闪存存储被链接，系统将在 <ItemLink id="gtceu:research_station" /> 完成研究后自动尝试将研究数据上传到可用的云研究数据机；研究站结构内的空气检测也已停止
* 所有云算力/研究数据系统都能够*跨维度*工作
