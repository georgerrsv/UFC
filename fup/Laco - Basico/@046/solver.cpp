#include <iostream>

int main() {
    
    int menor {};
    int maior {};
    
    std::cin >> menor >> maior;
    
    int a = menor;
    int b = maior;
    std::cout << "[ ";
    
    while ( b >= menor ) {
        std::cout << a << " " << b << ' ';
        a++;
        b--;
        
    }
    std::cout << "]\n";
    
}