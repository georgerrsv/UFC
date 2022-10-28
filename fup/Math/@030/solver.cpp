#include <iostream>

std::string calc(int value, int chute1, int chute2) {
    int dif1 = abs(chute1 - value);
    int dif2 = abs(chute2 - value);
    if (dif1 < dif2)
        return "primeiro\n";
    else if (dif1 > dif2)
        return "segundo\n";
    return "empate\n";
}

int main() {
    
    int value;
    int chute1, chute2;

    std::cin >> value >> chute1 >> chute2;
    std::string result = calc(value, chute1, chute2);
    std::cout << result;
}