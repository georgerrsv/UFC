#include <iostream>
#include <string>

std::string output(int a, int b, int c, int altura_janela, int largura_janela) {
    int tam_caixa = (a + b + c) / 3;
    int tam_janela = (altura_janela + largura_janela) / 2;

    if(tam_janela >= tam_caixa) {
        return "S\n";
    }
    return "N\n";
}

int main() {

    int a, b, c;
    int altura_janela, largura_janela;
    std::cin >> a >> b >> c;
    std::cin >> altura_janela >> largura_janela;
    std::string result = output(a, b, c, altura_janela, largura_janela);
    std::cout << result;
}