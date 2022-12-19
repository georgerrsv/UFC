#include <iostream>
#include <vector>

std::vector<int>filter(std::vector<int> jogadores, std::vector<int> escolha, int ordem) {
    std::vector<int> ganhador;
    int size = jogadores.size();
    for (int i = 0; i < size; i++) {
        if (escolha[i] == ordem)
            ganhador.push_back(jogadores[i]);
    }
    return ganhador;
}

int jogar(int jogador, int rodada) {
    std::vector<int> jogadores(jogador);
    for(int i = 0; i < jogador; i++) {
        std::cin >> jogadores[i];
    }
    while (rodada--) {
        
        int jogadas, ordem;
        std::cin >> jogadas >> ordem;
        std::vector<int> escolha(jogadas);
        for(int i = 0; i < jogadas; i++)
            std::cin >> escolha[i];
        jogadores = filter(jogadores, escolha, ordem);
    }
    return jogadores[0];
}


int main() {
    
    int n_teste { 1 };
    
    while (true) {
        int jogador {}, rodada {};
        std::cin >> jogador >> rodada;
        if(jogador == 0 && rodada == 0)
            break;
        std::cout << "Teste " << n_teste << '\n';
        std::cout << jogar(jogador, rodada) << '\n';
        n_teste++;
    }
}