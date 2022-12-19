#include <iostream>

string quadrado_perfeito(int x) {
    int n1 = 1;
    int n_total = 1;

    while(n_total < x){
        n1 += 2;
        n_total = n_total + n1;
    }

    if (x == n_total)
        return "sim\n";
    return "nao\n";
}

int main() {
    int num;
    std::cin >> num;
    std::string result = quadrado_perfeito(num);
    std::cout << result;
}

