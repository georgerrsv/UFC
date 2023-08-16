## @043 - Horas de sono


![](https://raw.githubusercontent.com/qxcodefup/arcade/master/base/043/cover.jpg)


## Ação

Faça um código que receba horas minutos e segundos tanto da hora atual e da hora do despertador e retorne quantas horas minutos e segundos você tem de sono.
Se o segundo horário for menor que o primeiro, compreenda que é no outro dia.
Se você dormir 23:00 e acorda às 6:00 então você tem 7:00 horas de sono.

### Entrada

- linha 1: hora minuto segundo (do horário que vai dormir).
- linha 2: hora minuto segundo (do horário que vai acordar).

### Saída

- hora minuto segundo (do tempo de sono que resta).

## Exemplos

```
>>>>>>>>
01 00 00
03 00 00
========
02 00 00
<<<<<<<<

>>>>>>>>
02 11 00
03 10 10
========
00 59 10
<<<<<<<<

>>>>>>>>
04 10 00
03 10 10
========
23 00 10
<<<<<<<<

>>>>>>>>
04 00 01
03 00 00
========
22 59 59
<<<<<<<<
```

