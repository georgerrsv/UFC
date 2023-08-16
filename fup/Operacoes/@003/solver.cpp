#include <iostream>

void desempenho(float velocidade, float tempo_min, float consumo) {

    float tempo_hora { tempo_min / 60 };
    float distancia = tempo_hora * velocidade;
    float desempenho = distancia / consumo;
    printf("%.2f\n", desempenho);
}

int main() {

    float velocidade, tempo_min, consumo;
    std::cin >> velocidade >> tempo_min >> consumo;
    desempenho(velocidade, tempo_min, consumo);
}