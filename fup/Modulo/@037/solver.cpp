#include <iostream>

std::string output(int play1, int play2) {
    if(play1 == play2)
        return "Empate\n";

    else if(play1 < play2 && play2 - play1 < 7)
        return "Jogador 1\n";
    
    else if(play1 > play2 && play1 - play2 > 7)
        return "Jogador 1\n";
    return "Jogador 2\n";
}

int main() {

    int play1, play2;
    std::cin >> play1 >> play2;

    std::cout << output(play1, play2);

}