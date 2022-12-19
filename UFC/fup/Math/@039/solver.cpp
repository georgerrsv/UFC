#include <iostream>

int main() {

	float jog1, valor_real;
	char jog2;
	std::cin >> jog1 >> jog2 >> valor_real;

	if (jog1 > valor_real && jog2 == 'm')
		std::cout << "segundo\n";
	else if (jog1 > valor_real && jog2 == 'M')
		std::cout << "primeiro\n";
	else if (jog1 < valor_real && jog2 == 'M')
		std::cout << "segundo\n";
	else if (jog1 < valor_real && jog2 == 'm')
		std::cout << "primeiro\n";
}