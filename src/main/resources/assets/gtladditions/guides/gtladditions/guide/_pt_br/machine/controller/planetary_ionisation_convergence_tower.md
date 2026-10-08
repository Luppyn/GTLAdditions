---
navigation:
  title: Torre de Convergência de Ionização Planetária
  icon: planetary_ionisation_convergence_tower
  parent: controller/multiblock_controller.md
  position: 10
item_ids:
  - planetary_ionisation_convergence_tower
---

# Torre de Convergência de Ionização Planetária

<BlockImage id = "planetary_ionisation_convergence_tower" scale = "8"/>

* Só podem ser usadas bobinas de grau Titânio ou superior;
* O ciclo operacional dura 3 segundos;
* Se energia continuar entrando enquanto o buffer interno de energia estiver cheio, ocorrerá uma explosão de raio de 100 blocos centrada na máquina, e dissipará uma quantidade de energia na rede de energia sem fio equivalente a 1.024 vezes a energia de pulso instantânea da bobina;
* No início do ciclo operacional, um pulso de EU _instantâneo_ de altíssima potência (1 tick) é injetado no buffer interno de energia, seguido por uma _descarga_ suave de menor potência no buffer pelo restante do ciclo;
* Após o pulso terminar, o buffer interno de energia irá liberar energia para o ambiente externo através da escotilha de energia/escotilha de fonte de laser:
* O nível do Contêiner Termodinâmico Estelar afeta a capacidade do buffer interno de energia:
> Básico: 890.000.000.000.000 EU \
> Avançado: 132.000.000.000.000.000 EU\
> Supremo: 1.570.000.000.000.000.000 EU
* O nível da bobina afeta o tipo de fluido consumido, a taxa de consumo por ciclo e a geração de energia
> Aço de Titânio a Ouro Requintado: <FluidLink id="gtceu:rhenium" /> 73.728 mB, <FluidLink id="gtceu:ice" /> 8 KB, <ItemLink id="kubejs:space_drone_mk2" /> 2×10⁻⁴ unidades \
> Taranium Naquadriático a Metal Estelar: <FluidLink id="gtceu:promethium" /> 36.864 MB, <FluidLink id="gtceu:liquid_helium" /> 4 KB, <ItemLink id="kubejs:space_drone_mk4" /> 1×10⁻⁴ unidades \
> Infinito a Eternidade: <FluidLink id="gtceu:crystalmatrix" /> 9216 MB, <FluidLink id="kubejs:gelid_cryotheum" /> 1 KB, <ItemLink id="kubejs:space_drone_mk6" /> 2,5×10⁻⁵ unidades \
>
> | Nível da Bobina        | Instantâneo(A MAX)    | Descarga(A MAX)   |
> |-----------------------|-----------------------|-------------------|
> | Aço de Titânio        | 4.096                 | 16                |
> | Adamantina            | 32.768                | 128               |
> | Taranium Naquadriático | 524.288              | 256               |
> | Metal Estelar         | 4.194.304             | 2.048             |
> | Infinito              | 8.388.608             | 4.096             |
> | Hipogênio             | 67.108.864            | 32.768            |
> | Eternidade            | 268.435.456           | 131.072           |
* Clique com o botão direito para inserir um na máquina através da <ItemLink id="gtmthings:creative_laser_hatch"/> portátil para ativar o modo de overclock especial:
> O ciclo operacional é reduzido para 1s; toda a energia é liberada diretamente para a rede sem fio, e a corrente máxima de saída por disparo é aumentada para 64A MAX+16, independentemente do nível da bobina e do buffer interno
* O consumo e os tipos de materiais neste momento são:
> <FluidLink id="gtceu:miracle" /> 10mB, <ItemLink id="kubejs:hyperdimensional_drone" /> 1x10^(-6) unidades
* **Nota**: Se o host for removido, o modo de overclock especial será redefinido e a Escotilha de Laser Criativa não será devolvida.