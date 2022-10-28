#include <iostream>

int main() {
    
    int dig;
    std::string num;
    std::cin >> dig  >> num;
    int size = num.size();
    int cont = 0;
    
    for (int i = 0; i < size; i++)
        if (num[i] == dig + '0')
            cont++;
    std::cout << cont << '\n';
}