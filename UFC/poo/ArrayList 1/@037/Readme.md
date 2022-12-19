## @037 Budega

![cover](https://raw.githubusercontent.com/qxcodepoo/arcade/master/base/037/cover.jpg)

Nosso objetivo no trabalho é modelar uma fila de atendimento de um Mercatil.

## Intro

- Quando o mercantil é incializado, é definido a quantidade de caixas que ele terá.
- Os caixas são modelados como um vetor de clientes de tamanho fixo. Uma posição do caixa ou terá o valor
null para indicar que o caixa está vazio ou terá um objeto cliente.
- A fila de espera é uma lista de clientes de tamanho variável. Todo cliente que chega é inserido no final da fila.
- As operações são entrar, chamarNoCaixa e finalizarAtendimento.

- Em Java
  - Os caixas devem ser implementados com um ArrayList e a fila de espera como um LinkedList.
- Em C++
  - Os caixas devem ser implementados com um vector e a fila de espera como um list.
  - Os clientes devem ser criados dinamicamente e gerenciados por um shared_ptr.