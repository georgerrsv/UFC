#include <iostream>

int main() {

	int angulo{ };

	std::cin >> angulo;

	if (angulo > 0) {

		int total = angulo % 360;
		std::cout << total << '\n';
	}
	else if (angulo < 0) {

		int total = 360 + angulo % 360;
		total = total % 360;

		std::cout << total << '\n';
	}
	else if (angulo == 0) {

		int total = 0;
		std::cout << total << '\n';
	}
}