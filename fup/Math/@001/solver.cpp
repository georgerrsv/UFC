#include <iostream>
#include <cmath>

int main() {
	
	float a { };
	float b { };
	float c { };

	std::cin >> a >> b >> c;

	float delta{ (b * b) - 4 * ( a * c) };

	if (delta > 0) {
		float raiz1 = ((b * (-1)) + sqrt(delta)) / (2 * a);
		float raiz2 = ((b * (-1)) - sqrt(delta)) / (2 * a);
		printf("%.2f\n%.2f\n", raiz1, raiz2);
	}
	else if (delta == 0) {
		float raiz1 = ((b * (-1)) + sqrt(delta)) / (2 * a);
		printf("%.2f\n", raiz1);
	}
	else {
		std::cout << "nao ha raiz real\n";
	}

}
