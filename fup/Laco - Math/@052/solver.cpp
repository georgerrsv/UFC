#include <iostream>

int main() {

    long long int atual = 1;
    long long int ult = 1;
    long long int penult = 1;
    int n;

    std::cin >> n;

    for(int i = 0; i < n - 2; i++) {
        atual = ult + penult;
        penult = ult;
        ult = atual;
    }
    std::cout << atual << '\n';
}