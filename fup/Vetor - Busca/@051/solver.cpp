#include <iostream>
#include <vector>

int main() {

    int size {};
    std::cin >> size;
    std::vector<int> pedra_a(size);
    std::vector<int> pedra_b(size);

    for(int i = 0; i < size; i++) {
        std::cin >> pedra_a[i] >> pedra_b[i];
    }

    int winner = -1;

    for(int i = 0; i < size; i++) {
        if(pedra_a[i] < 10 || pedra_b[i] < 10)
            continue;
        if(winner == -1)
            winner = i;
        if(abs(pedra_a[i] - pedra_b[i]) < abs(pedra_a[winner] - pedra_b[winner]))
            winner = i;
    }
    if(winner == -1)
        std::cout << "sem ganhador\n";
    else
        std::cout << winner << '\n';
}