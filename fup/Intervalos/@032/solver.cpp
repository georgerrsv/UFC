#include <iostream>

int main() {

	char tipo_saque{ };
	int forca{ };
	int poder{ };

	std::cin >> tipo_saque >> forca;

	if (tipo_saque == 'b') {

		poder = ((forca * 20) - 80) / 10;
		if (poder < 150)
			std::cout << "Fraco, nem passou\n";
		else if (poder >= 150 && poder < 180)
			std::cout << "Perfeito\n";
		else if (poder >= 180 && poder < 210)
			std::cout << "Satisfeito\n";
		else
			std::cout << "Muito forte, bola fora\n";
	}
	else if (tipo_saque == 'c') {

		poder = ((forca * 18) - 80) / 10;
		if (poder < 150)
			std::cout << "Fraco, nem passou\n";
		else if (poder >= 150 && poder < 180)
			std::cout << "Perfeito\n";
		else if (poder >= 180 && poder < 210)
			std::cout << "Satisfeito\n";
		else
			std::cout << "Muito forte, bola fora\n";
	}

}