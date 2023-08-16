#include <iostream>
#include <vector>
#include <algorithm>

int get_position(std::vector<int> vet, int elem) {
    for(int i = 0; i < (int) vet.size(); i++)
        if(vet[i] == elem)
            return i;
    return -1;
}

std::vector<int> get_types(std::vector<int> vet) {
    std::vector<int> sozinho;
    for(int i = 0; i < (int) vet.size(); i++) {
        if(i == get_position(vet, vet[i]))
            sozinho.push_back(vet[i]);
    }
    std::sort(begin(sozinho), end(sozinho));
    return sozinho;
}

std::vector<int> carregar_vetor(int num) {
    std::vector<int> vet;
    vet.reserve(num);
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
    std::vector<int> vet = carregar_vetor(size);
    std::vector<int> resp = get_types(vet);
    
    for(int i = 0; i < (int) resp.size(); i++)
        std::cout << (i == 0 ? "" : " ") << resp[i];
    std::cout << std::endl;
}