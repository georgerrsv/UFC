#include <iostream>

std::string output(int play1, int play2, int play3) {
    if(play1 == play2 && play2 == play3)
        return "empate\n";
    else if(play1 != play2 && play1 != play3)
        return "jog1\n";
    else if(play2 != play1 && play2 != play3)
        return "jog2\n";
    return "jog3\n";
}

int main() {

    int play1, play2, play3;
    std::cin >> play1 >> play2 >> play3;

    std::cout << output(play1, play2, play3);
}