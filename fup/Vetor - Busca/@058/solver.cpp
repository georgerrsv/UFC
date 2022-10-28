#include <iostream>

int main() {

    int size, min, max;
    int cont = 0;
    std::cin >> size >> min >> max;
    int vet[size];

    for(int i = 0; i < size; i++) {
        std::cin >> vet[i];
        if(vet[i] >= min && vet[i] <= max) {
            cont++;
        }
    }
    std::cout << cont << '\n';
}