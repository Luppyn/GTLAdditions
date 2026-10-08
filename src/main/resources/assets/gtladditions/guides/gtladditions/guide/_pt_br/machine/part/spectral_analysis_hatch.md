---
navigation:
  title: Escotilha de Análise Espectral
  icon: spectral_analysis_hatch
  parent: part/machine_part_index.md
  position: 10
item_ids:
  - gtladditions:spectral_analysis_hatch
---

# Escotilha de Análise Espectral

~~Também conhecida como Escotilha OP~~

<BlockImage id="spectral_analysis_hatch" scale="8" />

* Deve ser fabricada no nível de voltagem <Color color="#00AAAA">**UV**</Color>
* A Escotilha de Análise Espectral só pode ser instalada em um Processamento de Minério Integrado ou Processamento de Minério Integrado Avançado. É uma escotilha de peça adicional e apenas uma pode ser instalada na estrutura
* Ao abrir a GUI da escotilha, são exibidos três canais, cada um com três luzes indicadoras
* O número do canal de cada faixa é gerado aleatoriamente ~~(mas segue certos padrões)~~
* A quantidade de luzes indicadoras acesas após cada canal representa o nível de ativação correspondente, <Color color="#00FF00">verde indica estado ativo</Color>, <Color color="#FF0000">vermelho indica estado inativo</Color>
* Nível de Ativação 1 (intervalo de valor **±80**), Nível de Ativação 2 (intervalo de valor **±35**), Nível de Ativação 3 (intervalo de valor **±5**)
* Você pode ajustar o canal modificando o valor ou arrastando o controle deslizante abaixo da caixa de texto

* Canal 1: Bônus de Threads, aplicado diretamente às threads de processamento de múltiplas receitas
> **Processamento de Minério Integrado**: Nível 0 (bônus padrão): 4 threads, Nível 1: 6, Nível 2: 8, Nível 3: 10
>
> **Processamento de Minério Integrado Avançado**: Nível 0 (bônus padrão): 72 threads, Nível 1: 96, Nível 2: 128, Nível 3: 144
* Canal 2: Bônus de Probabilidade, todas as probabilidades de aumento de voltagem de saída probabilística são **multiplicadas diretamente** pelo nível do canal mais um
> Por exemplo: No Nível 2, ao produzir o item A com probabilidade base de saída de 30% e probabilidade base de bônus de voltagem de 5%, a probabilidade base de bônus de voltagem se torna (5 * (2 + 1)) = 15% após o bônus desta faixa
* Canal 3: Bônus Independente, bônus diferentes para Processamento de Minério Integrado e Processamento de Minério Integrado Avançado, bônus diferentes quando instalado em estruturas de máquinas diferentes
> Quando instalado em **Processamento de Minério Integrado**, obtém bônus de multiplicador de tempo de receita (**multiplicação direta**)
>
> Quando instalado em **Processamento de Minério Integrado Avançado**, obtém bônus de multiplicador de consumo de fluido (**multiplicação direta**)
>
> Multiplicador de bônus: Nível 0 (bônus padrão): 0.8, Nível 1: 0.65, Nível 2: 0.5, Nível 3: 0.4

* Além disso, quando o canal de entrada corresponde ao canal real (ou seja, erro zero), isso é chamado de Sintonia Perfeita
* Quando os três canais estão perfeitamente sintonizados, o overclock da máquina muda de overclock com perdas para overclock sem perdas e pode usar o Modo de Processamento Extremo para um processamento de receitas mais eficiente, aumentando drasticamente a eficiência de processamento da máquina
* ~~(Todos os três canais devem estar perfeitamente sintonizados para obter este bônus)~~
