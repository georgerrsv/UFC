#include <iostream>

int main() {
    
    int fundo_poco {};
    int salto {};
    int escorrega {};
    
    std::cin >> fundo_poco >> salto >> escorrega;
        
    int pos { 0 };
        
    while (true) {
        std::cout << pos;
        
        if (pos < 0) {
            std::cout << " morreu" << std::endl;
            break;
        }
        
        pos += salto;
        
        if(salto > 0) {
            
            salto -= 10;
        }
        if (pos >= fundo_poco) {
            std::cout << " saiu" << std::endl;
            break;
        }
        std::cout << " " << pos << std::endl;
        pos -= escorrega;
    }
}