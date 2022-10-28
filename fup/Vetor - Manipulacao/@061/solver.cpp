#include <iostream> 

int main() {
    
    int size;

    std::cin >> size;

    int vet[size];
    int vetReverso[size];

    for(int i = 0, j = size - 1; i < size; i++, j--) {
        std::cin >> vet[i];

        vetReverso[j] = vet[i];

    }
    std::cout << "[ ";
    for(int i = 0; i < size; i++) {
        std::cout << vetReverso[i] << " ";
    }
    std::cout << "]";
    std::cout << std::endl;
}