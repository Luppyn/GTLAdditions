---
navigation:
  title: Configuração de Máquinas do GTLAdditions
  parent: machine/machine_index.md
  position: 4
---

# Configuração de Máquinas do GTLAdditions

O número padrão de threads para a maioria das máquinas do GTLAdditions é 128 (quando aplicável; para referência, a máquina paralela entre receitas original usa 64 threads).

## **Modo de Divisão Igualitária**

> No Modo de Divisão Igualitária, a máquina processará todas as receitas possíveis, com as receitas paralelas distribuídas da forma mais uniforme possível \
> Se o tempo total da receita após a divisão igualitária exceder 1.000 segundos, o número de receitas executadas em paralelo não será distribuído igualmente; em vez disso, apenas uma receita que possa ser processada será executada \
> Neste modo, o número total de paralelos é: número de threads × número de paralelos da máquina
> Este modo não suporta processamento em lote

## **Modo Extremo**

> No Modo Extremo, a máquina se concentrará em processar uma parte das receitas, com overclock sem perdas e 1toc (para conceitos de overclock sem perdas e 1toc, consulte o livro de tarefas)\
> Neste modo, o bônus da Manutenção Configurável não terá efeito \
> Neste modo, o número de threads é o número máximo de receitas que podem ser processadas \
> Este modo ativa automaticamente o processamento em lote e não pode ser desativado \
> A menos que especificado de outra forma ou fornecido por um mecanismo específico, a operação das máquinas do GTLAdditions que não são máquinas paralelas entre receitas também segue o mesmo mecanismo do modo extremo

* Você pode selecionar o modo padrão na configuração do mod. O modo padrão inicial é o **Modo de Divisão Igualitária**.

#### **Configuração de Duração Limite para Receita**

> O botão pode ser aberto no canto inferior esquerdo da GUI de algumas máquinas do GTLAdditions para ajustar o valor padrão inicial. \
> O valor padrão inicial é 1 segundo. Ele varia de 5 ticks (mínimo) a 10 segundos (máximo). \
> O valor padrão também pode ser modificado no arquivo de configuração do mod.
