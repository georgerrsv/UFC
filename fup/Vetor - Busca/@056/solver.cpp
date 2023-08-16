#include <iostream>
#include <vector>

int main() {

    std::vector<int> vet;
    int size = 5;
    int menor;

    for(int i = 0; i < size; i++) {
        int value {};
        std::cin >> value;
        vet.push_back(value);
    }

    menor = vet[0];

    for(int i = 0; i < 5; i++) {
        if(vet[i] < menor)
            menor = vet[i];
    }
    std::cout << menor << '\n';
}