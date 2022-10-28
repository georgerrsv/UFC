#include <iostream>

int contaRepetidos(int a, int b, int c) {

    for(int i = 0; i < 3; i++) {
        if(a == b && b == c) {
            return 3;
        }
        else if(a != b && b != c && a != c) {
            return 0;
        }
    }
    return 2;
}

int main() {
    
        int a, b, c;
    
        std::cin >> a >> b >> c;
    
        std::cout << contaRepetidos(a, b, c) << '\n';
}