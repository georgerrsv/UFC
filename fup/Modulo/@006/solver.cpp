#include <iostream>

int main() {
    
    int jog1 {}, jog2 {}, jog3 {}, jog4 {};
    int pos = 0;
    
    std::cin >> jog1 >> jog2 >> jog3 >> jog4;

    int soma = jog1 + jog2 + jog3 + jog4;

    for(int i = 0; i < soma; i++) {
        pos++;
    }
    if(pos == 0)
        std::cout << "nenhum";
    if(pos % 4 == 1)
        std::cout << "jog1";
    if(pos % 4 == 2)
        std::cout << "jog2";
    if(pos % 4 == 3)
        std::cout << "jog3";
    if(jog1 == jog2 && jog1 == jog3 && jog1 == jog4 && pos > 0)
        std::cout << "jog4";
        
    std::cout << std::endl;
    return 0;
}