#include <iostream>

int mod (int valor, int total) {

    valor = valor % total;

    return valor > 0 ? valor : valor + total;

}

int main() {

    int hora_ini;
    int minuto_ini;
    char sentido;
    int distancia;

    std::cin >> hora_ini >> minuto_ini >> sentido >> distancia;

    int posicao = (hora_ini * 6) + (minuto_ini / 10);
    posicao += sentido == 'H' ? +distancia : -distancia;
    posicao = mod(posicao, 12 * 6);

    int hora = posicao / 6;
    int minuto = (posicao % 6) * 10;

    printf("%02d %02d\n", hora, minuto);

}