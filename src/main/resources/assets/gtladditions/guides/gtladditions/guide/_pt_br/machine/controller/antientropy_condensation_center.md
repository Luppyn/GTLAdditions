---
navigation:
  title: Condensação de Antientropia
  icon: antientropy_condensation_center
  parent: controller/multiblock_controller.md
  position: 10
item_ids:
  - antientropy_condensation_center
---

# Condensação de Antientropia

<BlockImage id = "antientropy_condensation_center" scale = "4"/>

* Esta máquina consome Pó de Cryotheum antes de cada operação. A quantidade consumida é calculada pela fórmula:

> <Latex math = "Cryotheum Dust Consumption = \frac{5 * (\frac{Recipe Parallel}{2^{19}} + 51 * \ln{Recipe Parallel})}{Voltage Tier - 9}" />

* Você pode segurar <ItemLink id="kubejs:create_ultimate_battery" /> e clicar com o botão direito para inserir uma na máquina e obter os seguintes bônus adicionais:
* Multiplicador de tempo: 0.7; Multiplicador de energia: 0.5
* **Nota**: O efeito de bônus será redefinido se a máquina for removida e a Bateria Ultimate Criativa não será devolvida
