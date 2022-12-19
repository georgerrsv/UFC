#include <iostream>
#include <vector>

void show_vector(std::vector<int> vet) {
    
    int size = vet.size();
    
    for(int i = 0; i < size; i++) {
        std::cout << vet[i];
    }
}
std::vector<int> load_vector(int num) {
    std::vector<int> vet;
    for(int i = 0; i < num; i++) {
        int value {};
        std::cin >> value;
        vet.push_back(value);
    }
    return vet;
}


int main() {

    int size;
    std::cin >> size;
    std::vector<int> vet = load_vector(size);
    show_vector(vet);
    std::cout << endl;
}