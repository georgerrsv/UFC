#include <iostream>
#include <vector>

std::string jediOrSith(std::vector<int> v, int value, int size) {
    int first = 0, second = 0;

    for(int i = 0; i < size/2; i++) {
        first += v[i];
    }
    for(int i = size/2; i < size; i++) {
        second += v[i];
    }
    if(first > second)
        return "Jedi\n";

    else if(first < second)
        return "Sith\n";

    return "Empate\n";
}

int main() {
    int size, value;
    std::vector<int> v;

    std::cin >> size;
    for(int i = 0; i < size; i++) {
        std::cin >> value;
        v.push_back(value);
    }

    std::cout << jediOrSith(v, value, size);

    return 0;
}