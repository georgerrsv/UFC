## @032 - Bolada na fuça


![Resultado de imagem para haikyuu](https://raw.githubusercontent.com/qxcodefup/arcade/master/base/032/cover.jpg)

## Motivação

A fórmula é dada por:

P = ((F \* T) - 80) / 10

* P é o poder
* F a força
* T é a força para cada tipo de saque

- Se tipo for
    - b (por baixo), T tem valor 20.
    - c (por cima), T tem valor 18.

Com isso, ele concluiu uma faixa de satisfação dos saques:

* Se o poder for inferior a 150, "Fraco, nem passou".
* Se for maior ou igual a 150 e inferior 180, "Perfeito".
* Se for entre 180 e 210 "Satisfeito".
* Caso seja superior a 210, "Muito forte, bola fora".

Desenvolva o programa que dados os valores de entrada, imprima o resultado de satisfação.

### Entrada

* Tipo de saque (c ou b) do tipo char
 
* Um inteiro para a força do atleta

### Saída

* A precisão do saque do atleta

## Exemplos:

```
>>>>>>>>
c
100
========
Perfeito
<<<<<<<<

>>>>>>>>
b
68
========
Fraco, nem passou
<<<<<<<<

>>>>>>>>
c
160
========
Muito forte, bola fora
<<<<<<<<

>>>>>>>>
b
99
========
Satisfeito
<<<<<<<<
```
