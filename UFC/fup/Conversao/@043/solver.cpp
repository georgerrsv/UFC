#include <iostream>

int main() {

    int hora1, minuto1, segundo1;
    int hora2, minuto2, segundo2;

    std::cin >> hora1 >> minuto1 >> segundo1;
    std::cin >> hora2 >> minuto2 >> segundo2;

    int total1 = (hora1 * 60 * 60) + (minuto1 * 60) + segundo1;
    int total2 = (hora2 * 60 * 60) + (minuto2 * 60) + segundo2;

    if (total2 < total1) {

        total2 += 24 * 60 * 60;
        int result = total2 - total1;
        int hora = result / (60 * 60);
        int resto = result % (60 * 60);
        int minuto = resto / 60;
        int segundo = resto % 60;
        printf( "%02d %02d %02d\n", hora, minuto, segundo);
    }
    else {

        int result = total2 - total1;
        int hora = result / (60 * 60);
        int resto = result % (60 * 60);
        int minuto = resto / 60;
        int segundo = resto % 60;
        printf( "%02d %02d %02d\n", hora, minuto, segundo);
    }
}