#include <iostream>

int main() {

    int num1 {};
    int num2 {};

    std::cin >> num1 >> num2;

    int div = num1 / num2;
    int resto = num1 % num2;
    float div_resto = (float)num1 / num2;

    printf("%d\n%d\n%.2f\n", div, resto, div_resto);

}