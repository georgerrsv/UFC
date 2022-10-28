#include <iostream>
#include <vector>
#include <algorithm>

int main() {

    std::vector<int> vet;

    for(int i = 0; i < 3; i++) {
        int value {};
        std::cin >> value;
        vet.push_back(value);
    }
    std::sort(begin(vet), end(vet));
    std::cout << vet[1] << '\n';
}