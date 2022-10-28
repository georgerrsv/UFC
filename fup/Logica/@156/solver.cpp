#include <iostream>

std::string output(int p, int d1, int d2) {
    if(p == 0) {
        int sum = d1 + d2;
        if(sum % 2 == 0)
            return "0\n";
        else
            return "1\n";
    }
    else {
        int sum = d1 + d2;
        if(sum % 2 == 0)
            return "1\n";
    }
    return "0\n";
}

int main() {

	int p, d1, d2;
    std::cin >> p >> d1 >> d2;

    std::cout << output(p, d1, d2);
    
}