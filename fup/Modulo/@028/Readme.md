## @028 - Cabeça da cobra

![](https://raw.githubusercontent.com/qxcodefup/arcade/master/base/028/cover.jpg)

## Descrição

No jogo da cobrinha, quando a cabeça passa do limite direito, ela reaparece do lado esquerdo. Quando passa do limite inferior, reaparece na parte de cima. Imagine o jogo apenas com a cabeça da cobra. A tela é quadrada, formada por N quadrados de largura e N quadrados de altura. O quadrado de posição 0, 0 é o mais em cima na esquerda. O X cresce para direita e o Y para baixo de acordo com a seguinte figura.

![](https://raw.githubusercontent.com/qxcodefup/arcade/master/base/028/__pontos.jpg)

A cabeça da cobra pode estar apontada para 4 possíveis direções. \[U\] Up(Cima), \[D\] Down (Baixo), \[L\] Left (Esquerda), \[R\] Right (Direita). Mavarildo se distrai por S segundos. Imagine que cada segundo, a cabeça da cobra se move 1 posição. Você deve fazer um código que calcule a posição da cabeça da cobra dada a dimensão do tabuleiro N, a posição inicial X, Y, a direção da cabeça C e a quantidade de segundos S que Mavarildo passa distraído.

### Entrada

- N, X, Y, C, S, um por linha.

### Saída

- X Y da posição final da cobra

## Restrições

* 0 ≤ N, X, Y, C, S ≤ 1000

## Exemplos

```
>>>>>>>>
10
4
3
R
1
========
5 3
<<<<<<<<

>>>>>>>>
10
4
3
R
8
========
2 3
<<<<<<<<

>>>>>>>>
10
4
5
U
1
========
4 4
<<<<<<<<
```