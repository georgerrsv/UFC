#include <iostream>
#include <cmath>

int main() {
    
    char op;
    float num;
    
    std::cin >> op >> num;
    
    if (op == 'r'){
        
        std::cout << round(num) << '\n';
        
    }else if (op == 'f') {
        
        std::cout << floor(num) << '\n';
        
    }else {
        
        std::cout << ceil(num) << '\n';
    }
    
}