#include <iostream>

std::string output(int linha, int coluna) {
    if(linha % 2 == 0 && coluna % 2 == 0) {
        return "1\n";
    }
    else if(linha % 2 == 0 && coluna % 2 != 0) {
        return "0\n";
    }
    else if(linha % 2 != 0 && coluna % 2 == 0) {
        return "0\n";
    }
    return "1\n";
}

int main() {

    int linha, coluna;
    std::cin >> linha >> coluna;

    std::cout << output(linha, coluna);

}