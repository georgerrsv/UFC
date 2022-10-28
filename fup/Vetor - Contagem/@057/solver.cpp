#include <iostream>
#include <vector>

std::string soldierOrRebel(std::vector<int> v, int value, int size) {
    int soldier = 0, rebel = 0;

    for(int i = 0; i < size; i++) {
        if(v[i] % 2 == 0)
            soldier+=v[i];
        if(v[i] % 2 != 0)
            rebel+=v[i];
    }
    if(soldier == rebel)
        return "empate\n";
    else if(soldier > rebel)
        return "rebeldes\n";
    return "soldados\n";
}

int main() {
    int size, value;
    std::vector<int> v;

    std::cin >> size;
    for(int i = 0; i < size; i++) {
        std::cin >> value;
        v.push_back(value);
    }

    std::cout << soldierOrRebel(v, value, size);

    return 0;
}