#include <iostream>
#include <vector>

std::string name_card(int value) {

    std::vector<string> name = {"", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};

    return name[value];
}

void show_card(std::vector<int> hand) {
    std::cout << "[";
    for(int i = 0; i < (int) hand.size(); i++) {
        std::cout << (i == 0 ? "" : ", ") << name_card(hand[i]);
    }
    std::cout << "]";
}

int main() {

    std::vector<int> hand;
    int carta;
    int size;
    std::cin >> size;

    for(int i = 0; i < size; i++) {
        std::cin >> carta;
        hand.push_back(carta);
    }
    show_card(hand);
    std::cout << std::endl;
}