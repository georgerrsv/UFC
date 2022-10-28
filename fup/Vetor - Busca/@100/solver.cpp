#include <iostream>
#include <vector>

int main() {

    std::vector<int> vet;
    int qtd_jog;
    int winner = -1;
    int tam;
    std::cin >> tam >> qtd_jog;

    
    for(int i = 0; i < qtd_jog; i++) {
        int value {};
        std::cin >> value;
        vet.push_back(value);
        if(vet[i] > tam)
            continue;
        if(vet[i] <= tam) {
            vet.push_back(value);
        }
        if(winner == -1)
            winner = i;
        if(abs(vet[i] - tam) < abs(vet[winner] - tam))
            winner = i;
    }
    if(winner == -1)
        std::cout << "nenhum";
    else
        std::cout << winner;
}