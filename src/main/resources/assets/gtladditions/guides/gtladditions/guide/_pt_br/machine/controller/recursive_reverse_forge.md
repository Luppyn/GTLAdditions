---
navigation:
  title: Forja Reversa Recursiva
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

# Forja Reversa Recursiva

<BlockImage id = "recursive_reverse_forge" scale = "8"/>

* Fator de consumo de energia: 0.8
* Número máximo de paralelos: 2.147.483.647
* Possui [Tipos de Receita Multibloco](../multi_type.md): Forja de Plasma Dimensionalmente Transcendente, Forja Estelar
* Overclock perfeito, e o número de overclocks é ilimitado
* Apenas a câmara de laser pode ser usada
* Módulos podem ser instalados para obter bônus adicionais

### Motor de Amplificação Temporal Reversa

<BlockImage id = "reverse_time_boosting_engine" scale = "4"/>

* **Só pode ser instalado na estrutura da Forja Reversa Recursiva, e apenas um deste módulo pode ser instalado em cada Forja Reversa Recursiva**

> Após instalar o módulo, o tempo da receita pode ser reduzido por um fator de: \
> <Latex math = "\min{(0.8, 0.05+0.8*e^{-3.2*input ratio^{1.9}})}" /> \
> A proporção de entrada é: quantidade de entrada multiplicada por 2/(quantidade de saída inicial da receita * temperatura atual), a proporção de entrada não será maior que 1, e a função de redução de tempo não será ativada quando a proporção de entrada for menor que 10% (A quantidade de saída inicial da receita refere-se à saída de uma receita executada em 1 paralelo sem bônus adicionais)\
> Basta inserir um item ou fluido de saída. Não use <FluidLink id="gtceu:dimensionallytranscendentresidue" />,<ItemLink id="kubejs:extremely_durable_plasma_cell" />,<ItemLink id="kubejs:time_dilation_containment_unit" />, <ItemLink id="kubejs:plasma_containment_cell" /> \
> A temperatura inicial é 48000K, se a máquina estiver em estado de funcionamento, a temperatura aumentará a uma velocidade de 65K/t, e em estado não funcional, a temperatura diminuirá a uma velocidade de 900K/s (não inferior a 48000K) \
> Diferentes fluidos podem ser introduzidos para controlar a temperatura. O meio de aquecimento pode ser <FluidLink id="minecraft:lava" />2500K,<FluidLink id="gtceu:blaze" />4600K,<FluidLink id="gtceu:raw_star_matter" />14000K, e o fluido de resfriamento pode ser <FluidLink id="gtceu:ice" />1900K,<FluidLink id="gtceu:helium" />3400K,<FluidLink id="kubejs:gelid_cryotheum" />6700K \
> As taxas de consumo tanto do meio de aquecimento quanto do fluido de resfriamento são 100B/1s \
> Os produtos da receita inseridos serão devolvidos proporcionalmente após a conclusão do processamento da receita \
> Quando a temperatura estiver dentro do intervalo de [93000K, 97000K], a proporção de retorno é 100% \
> Quando a temperatura for inferior ao limite inferior do intervalo, a proporção de retorno é:  \
> <Latex math = "0.5+0.5*\frac{current temperature-48000}{45000}" /> \
> Quando a temperatura exceder o limite superior do intervalo, a proporção de retorno é: \
> <Latex math = "1-0.85*(\frac{current temperature-97000}{13000})^{0.42}" /> \
> O mecanismo de proteção contra superaquecimento será acionado quando a temperatura exceder 105000K. Por padrão, a temperatura é reduzida a uma taxa de resfriamento de 7125K/s (usar fluido de resfriamento pode aumentar a taxa de resfriamento adicionalmente; a taxa de resfriamento real é a taxa padrão mais a taxa de resfriamento do fluido de resfriamento). A Forja Reversa Recursiva vinculada não processará a receita até que caia para 48000K \
> O <ItemLink id="gtladditions:vientiane_transcription_node" /> pode ser instalado para controlar a temperatura, semelhante ao sensor de nêutrons \
> **Apenas** use o compartimento de entrada gigante para fornecer o fluido de controle de temperatura. **Apenas** use <ItemLink id="super_input_dual_hatch" /> para fornecer entrada ao produto da receita

### Matriz de Cascata Catalítica

<BlockImage id = "catalytic_cascade_array" scale = "4"/>

* **Só pode ser instalado na estrutura da Forja Reversa Recursiva, e apenas um deste módulo pode ser instalado em cada Forja Reversa Recursiva**

> Após instalar este módulo, o consumo de energia da receita pode ser multiplicado por 0.15, e a saída da receita pode ser dobrada \
> Ele tem um **período de ciclo** de catalisador de 30 segundos. No início de cada ciclo de catalisador, o módulo emitirá aleatoriamente um sinal de redstone variando de 1 a 15 \
> O sinal de redstone emitido precisa ser recebido através do <ItemLink id="gtladditions:vientiane_transcription_node" /> \
> **Apenas** use o Compartimento de Entrada Gigante LV para receber o catalisador de entrada \
> Se o sinal de redstone for de 1 a 3, isso indica que o catalisador usado neste ciclo é <FluidLink id="gtceu:dimensionallytranscendentcrudecatalyst" />. Seguindo este padrão, as ordens subsequentes são <FluidLink id="gtceu:dimensionallytranscendentprosaiccatalyst" />, 
> <FluidLink id="gtceu:dimensionallytranscendentresplendentcatalyst" />, <FluidLink id="gtceu:dimensionallytranscendentexoticcatalyst" /> e <FluidLink id="gtceu:dimensionallytranscendentstellarcatalyst" /> \
> Durante os primeiros 0 a 5 segundos do ciclo, o módulo não funcionará. Após 5 segundos, o módulo consumirá o catalisador com base no sinal de redstone emitido. A taxa de consumo do catalisador é 40B/s, e o efeito durará até o quinto segundo do próximo ciclo \
> Se o catalisador errado for inserido, não haverá aumento na produção pelo resto do ciclo e qualquer catalisador inserido subsequentemente será consumido, e o efeito de redução de energia será mantido \
> O processamento atual e subsequente de receitas contendo <ItemLink id="kubejs:extremely_durable_plasma_cell" />,<ItemLink id="kubejs:time_dilation_containment_unit" /> e <ItemLink id="kubejs:plasma_containment_cell" /> não será incluído no processo de duplicação \
> **O módulo Núcleo de Convergência Magnetoreológica tem prioridade maior que este módulo**

### Núcleo de Convergência Magnetoreológica

<BlockImage id = "magnetorheological_convergence_core" scale = "4"/>

* **Só pode ser instalado na estrutura da Forja Reversa Recursiva, e apenas um deste módulo pode ser instalado em cada Forja Reversa Recursiva**

> Após instalar este módulo, a saída da receita pode ser focada no primeiro item e fluido, convertendo a saída do segundo produto em saída adicional do primeiro produto \
> Ele tem um ciclo de entrada de combustível de 12 segundos, e **apenas** dois compartimentos de entrada gigantes ULV e um compartimento de entrada gigante LV podem ser usados para receber o combustível \
> Quando o módulo é ativado pela primeira vez, ele selecionará aleatoriamente dois itens e um fluido de <ItemLink id="kubejs:black_body_naquadria_supersolid" />,<ItemLink id="kubejs:quantum_anomaly" />,<ItemLink id="kubejs:hyper_stable_self_healing_adhesive" />,<FluidLink id="gtceu:exciteddtec" /> e <FluidLink id="gtceu:exciteddtsc" /> como o combustível para manter a operação do módulo \
> O combustível correto selecionado pelo módulo precisa ser inserido com precisão para ativar a função de foco. Se a quantidade inserida estiver incorreta, uma mensagem de erro será exibida na GUI do módulo \
> Ao mesmo tempo, 2/s de Bloco de Magmatéria são consumidos fixamente. Se a entrada for insuficiente, a receita não poderá ser focada e a saída será impossível \
> O processamento atual e subsequente de receitas contendo <ItemLink id="kubejs:extremely_durable_plasma_cell" />,<ItemLink id="kubejs:time_dilation_containment_unit" /> e <ItemLink id="kubejs:plasma_containment_cell" /> não será incluído no processo de duplicação \
> **O módulo Motor de Amplificação Temporal Reversa tem prioridade maior que este módulo**

### Concentrador de Energia Hiperdimensional

<BlockImage id = "hyperdimensional_energy_concentrator" scale = "4"/>

* **Só pode ser instalado na estrutura da Forja Reversa Recursiva, e apenas um deste módulo pode ser instalado em cada Forja Reversa Recursiva**

> Após o módulo ser instalado, a Forja Reversa Recursiva pode funcionar diretamente obtendo energia da rede de energia sem fio \
> O <ItemLink id="kubejs:hyperdimensional_drone" /> deve ser colocado no módulo principal. Cada vez que for colocado, a energia máxima obtenível aumentará em 16A 
> <Color color="#FF0000">**M**</Color><Color color="#00FF00">**A**</Color><Color color="#0000FF">**X**</Color><Color color="#FFFF00">**+**</Color><Color color="#FF0000">**16**</Color> \
> A potência máxima que pode ser obtida pela base é 1A MAX, e é necessário colocar o Drone Hiperdimensional para aumentar o limite superior de potência (isso também travará o nível da receita em MAX), e o máximo que pode ser colocado é 64 \
> Um drone hiperdimensional é lançado (consumido) a cada hora para manter a conexão com a rede de energia sem fio \
> É necessário fornecer 524.288 CWU/t, 64A <Color color="#FF0000">**MAX**</Color> e 240B/s de Criotéum Gélido para manter a operação do módulo

### Manipulador Fractal

<BlockImage id = "fractal_manipulator" scale = "4"/>

* **Só pode ser instalado na estrutura da Forja Reversa Recursiva, e cada Forja Reversa Recursiva pode acomodar no máximo quatro destes módulos**

> Fator de consumo de energia: 0.8 \
> Número máximo de paralelos: 2.147.483.647 \
> Overclock perfeito, e o número de overclocks é ilimitado \
> Apenas a câmara de laser pode ser usada \
> Ele pode compartilhar a Matriz de Cascata Catalítica e o Concentrador de Energia Hiperdimensional com a Forja Reversa Recursiva \
> Este módulo funciona **se e somente se** o módulo Motor de Amplificação Temporal Reversa estiver funcionando perfeitamente \
> Cada execução requer o consumo de um acelerador, não participa do cálculo paralelo, e retorna após a conclusão da receita
