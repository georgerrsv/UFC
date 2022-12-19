#include <iostream>

int output(int angulo) {
    if(angulo > 0) {
        return angulo % 360;
    }
    else if(angulo < 0) {
        int total = 360 + (angulo % 360);
        total = total % 360;
        return total;
    }
    return 0;
}

int main() {

    int angulo;
    std::cin >> angulo;

    std::cout << output(angulo) << '\n';
}