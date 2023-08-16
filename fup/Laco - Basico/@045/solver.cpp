#include <iostream>

int main() {

	int a { };
	int b { };
	int soma { 0 };

	std::cin >> a >> b;

	if (b >= a) {

		for (int i = a; i <= b; i++) {

			if (i % 2 == 0)
				soma += i;
		}
		std::cout << soma << '\n';
	}
	else if (b < a)
		std::cout << "invalido\n";
}