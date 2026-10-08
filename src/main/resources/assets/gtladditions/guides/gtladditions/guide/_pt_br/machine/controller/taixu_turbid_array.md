---
navigation:
  title: Matriz de Turbidez Taixu
  icon: taixu_turbid_array
  parent: controller/multiblock_controller.md
  position: 10
item_ids:
  - taixu_turbid_array
---

# Matriz de Turbidez Taixu

<BlockImage id = "taixu_turbid_array" scale = "8"/>

> Você pode abrir a GUI do controlador principal e colocar os Enxames Nano correspondentes ou a Escotilha de Energia Criativa no slot de item no canto inferior direito da GUI \
> Ao colocar uma **Escotilha de Energia Criativa**, colocar uma concederá 3^16 de paralelismo e 100% de bônus de taxa de sucesso (~~colocar várias tem o mesmo efeito~~) \
> Ao colocar os Enxames Nano correspondentes, você obtém um bônus adicional de taxa de sucesso, sendo o valor do bônus o número de Enxames Nano colocados × bônus base \
> Você pode colocar até 64 Enxames Nano ou Escotilhas de Energia Criativa \
> Ao colocar **Enxame Nano do End**, o bônus base é 0.01 \
> Ao colocar **Enxame Nano de Dragão**, o bônus base é 0.05 \
> Ao colocar **Enxame Nano do Espaço-Tempo**, o bônus base é 0.1 \
> Ao colocar **Enxame Nano Eterno**, o bônus base é 0.2

* Esta estrutura de máquina pode ter apenas uma Escotilha de Laser
* Quando o nível de voltagem da máquina for maior ou igual a <Color color="#FFFF00">**UXV**</Color>, a saída de **Amplificador UU** é desbloqueada
* Quando o nível de voltagem da máquina for maior ou igual a <Color color="#FF0000">**MAX**</Color>, a saída de **Matéria UU** é desbloqueada
* ~~Quando o nível de voltagem da máquina não for atingido, não haverá saída adicional de Amplificador UU ou Matéria UU~~
* O consumo fixo de energia da máquina é 524.288 vezes a potência correspondente ao seu nível de voltagem atual; o tempo de operação padrão é de 5 segundos, reduzido para 1 segundo quando colocada na Câmara de Criação de Energia.

> **~~Aviso de muitas fórmulas~~**

* Fórmula de cálculo do bônus α por nível de Contêiner Térmico Estelar:
> <Latex math = "\alpha = 8 * (2^{Stellar Containment Tier} - 1) * \sqrt{Voltage Tier + 1}" />

* Fórmula de cálculo do bônus β por nível de Bobina:
> <Latex math = "\beta = 3.8 * 1.3^{Coil Level} * (\frac{Coil Temperature}{36000})^{0.7}" />

* Fórmula de cálculo da probabilidade de sucesso do Amplificador UU:
> <Latex math = "1/(1 + e^{-0.1 * (\frac{\alpha}{50} + \frac{\beta}{100} + \frac{height}{3})})" />

* Fórmula de cálculo da saída base do Amplificador UU:
> <Latex math = "40960 * \tanh{(0.007 * (\alpha * \frac{height}{9} + \sqrt{\beta} * \ln{(Voltage Tier + 2)}))}" />

* Fórmula de cálculo da probabilidade de sucesso da Matéria UU:
> <Latex math = "1/(1 - e^{-0.02 * (\frac{\alpha + \beta}{20} + \sqrt[3]{height} * \frac{Voltage Tier}{3})})" />

* Fórmula de cálculo da saída base da Matéria UU:
> <Latex math = "22500 * \tanh{(\sqrt{\alpha * \beta} * \frac{(height + Voltage Tier) * 0.045}{200})}" />

* Fórmula de cálculo do paralelismo da máquina:
> <Latex math = "4096 * 1.621^{\min(\frac{Coil Temperature}{6400},12)}" />

* **Nota**: A altura nas fórmulas refere-se à altura das camadas repetidas na estrutura, semelhante à altura de uma Torre de Destilação ou Ativador de Nêutrons
