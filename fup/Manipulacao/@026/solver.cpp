#include <iostream>
#include <string>

std::string descobre(int value) {
	if (value < 0)
		return "negativo\n";
	else if (value == 0)
		return "nulo\n";

    return "positivo\n";
}

int main() {

	int value;
	std::cin >> value;
	std::string result = descobre(value);
    std::cout << result;
}