#include <iostream>

std::string output(char play1, char play2) {
    if(play1 == play2)
        return "empate\n";
    else if(play1 == 'R' && play2 == 'S')
        return "jog1\n";
    else if(play1 == 'S' && play2 == 'P')
        return "jog1\n";
    else if(play1 == 'P' && play2 == 'R')
        return "jog1\n";
    return "jog2\n";
}

int main() {

    char play1, play2;
    std::cin >> play1 >> play2;

    std::cout << output(play1, play2);
    
}