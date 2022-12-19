#include <iostream>

int main() {
    
    int n, x, aux = 0;

    std::cin >> x >> n;

    int value[n];

    for(int i = 0; i < n; i++) {
        std::cin >> value[i];
    }
    for(int i = 0; i < n; i++) {
        if(value[i] == x) {
            aux++;
        }
    }
    std::cout << aux << '\n';
}