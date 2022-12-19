#include <iostream>

void soma(int num1, int num2) {
    int soma;
    soma = num1 + num2;
    std::cout << soma;
}
void subtrai(int num1, int num2) {
    int sub;
    sub = num1 - num2;
    std::cout << sub;
}
void multiplica(int num1, int num2) {
    int mult;
    mult = num1 * num2;
    std::cout << mult;
}
void divide(int num1, int num2) {
    double divide;
    divide = (double)num1 / (double)num2;
    printf("%.2f", divide);
}
void resto(int num1, int num2) {
    int resto;
    resto = num1 % num2;
    std::cout << resto;
}

int main() {

    int num1, num2;

    std::cin >> num1 >> num2;

    soma(num1, num2);
    std::cout << std::endl;
    subtrai(num1, num2);
    std::cout << std::endl;
    multiplica(num1, num2);
    std::cout << std::endl;
    divide(num1, num2);
    std::cout << std::endl;
    resto(num1, num2);
    std::cout << std::endl;

    return 0;
}