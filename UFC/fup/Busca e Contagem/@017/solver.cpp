#include <iostream>
#include <vector>

int main() {

    std::vector<int> vet;

    for(int i = 0; i < 4; i++) {
        int value {};
        std::cin >> value;
        vet.push_back(value);
    }
    int maior = vet[0];
    for(int i = 0; i < 4; i++) {
        if(vet[i] > maior) {
            maior = vet[i];
        }
    }
    std::cout << maior << '\n';
}