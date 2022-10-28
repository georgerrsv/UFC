#include <iostream>

std::string output(int n1, int n2) {
    if(n1 % 3 == 0 && n2 % 3 == 0 || n1 % 5 == 0 && n2 % 5 == 0) {
        return "sim\n";
    }
    return "nao\n";
}

int main() {

	int n1, n2;
    std::cin >> n1 >> n2;
    std::cout << output(n1, n2);
}