#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> reverso(std::vector<int> vet, int num) {
    int uni;

    while(true) {
        
        uni = num % 10;
        vet.push_back(uni);
        if (num < 10)
            break;
        num = num / 10;
    }
    reverse(vet.begin(), vet.end());

    return vet;
}

int main() {
    
    int num;
    std::vector<int> vet;
    std::cin >> num;

    std::vector<int> result = reverso(vet, num);
    int size = result.size();

    for(int i = 0; i < size; i++) {
        std::cout << (i == 0 ? "" : " ") << result[i];
    }
    std::cout << endl;
}