#include <iostream>

int main() {

    int vet[5];
    int menor;
    int maior;
    int soma;


    for(int i = 0; i < 5; i++) {
        std::cin >> vet[i];
    }
    menor = vet[0];
    maior = vet[0];

    for(int i = 0; i < 5; i++) {
        if(vet[i] > maior)
            maior = vet[i];
        if(vet[i] < menor)
            menor = vet[i];
        soma = menor + maior;
    }
    std::cout << soma << '\n';
}