#include <iostream>
#include <string>

std::string impedimento(int jog_l, int jog_r, int jog_d) {

    if (jog_r > 50 && jog_l < jog_r && jog_r > jog_d)
        return "S\n";
    return "N\n";
}

int main() {

	int jog_l, jog_r, jog_d;
    std::cin >> jog_l >> jog_r >> jog_d;
    std::string result = impedimento(jog_l, jog_r, jog_d);
    std::cout << result;
}