#include <iostream>

int main() {

    int primeiro = 0;
    int segundo = 1;
    int soma = 0;
    int n;
    int soma_par = 0;
    
    std::cin >> n;

    soma = primeiro + segundo;

    while(soma <= n) {

        if(soma % 2 == 0) {
            soma_par+=soma;
        }

        primeiro = segundo;
        segundo = soma;
        soma = primeiro + segundo;
    }
    std::cout << soma_par << '\n';
}