#include <iostream>

int main() {

    int c { 0 }, m { 0 };
    int cont { 0 };
    std::cin >> c;

    while(cont < (2 * c)) {
        std::cin >> m;
        cont += m;
        if(cont >= (2 * c)){
            std::cout << "hora de partir\n";
            break;
        }
        else if(cont >= c){
            std::cout << "lotado\n";
        }
        else if(cont == 0) {
            std::cout << "vazio\n";
        }
        else if(cont < c) {
            std::cout << "ainda cabe\n";
        }
    }
}