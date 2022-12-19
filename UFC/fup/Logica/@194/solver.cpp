#include <iostream>

std::string output(int b, int t) {
    int cut = ((b + t) * 70) / 2;
    int half = (160 * 70) / 2;

    if (cut < half)
        return "2\n";

    else if (cut > half)
        return "1\n";

    return "0\n";
}

int main() {

    int b, t;
    std::cin >> b >> t;

    std::cout << output(b, t);
}