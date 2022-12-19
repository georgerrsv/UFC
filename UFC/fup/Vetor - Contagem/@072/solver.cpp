#include <iostream>

int main() {
    
    int size;
    double sum = 0;
    double media = 0;
    std::cin >> size;
    double vet[size];

    for(int i = 0; i < size; i++) {
        std::cin >> vet[i];
        sum += vet[i];
        media = double(sum) / double(size);
    }
    printf("%.2f\n", media);
    for(int i = 0; i < size; i++) {
        if(i != 0)
            std::cout << " ";
        if(vet[i] == media)
            std::cout << "M";
        if(vet[i] < media)
            std::cout << "P";
        if(vet[i] > media)
            std::cout << "G";
    }
    std::cout << std::endl;
}