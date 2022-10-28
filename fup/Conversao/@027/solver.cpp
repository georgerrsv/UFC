#include <iostream>

int main() {
    
	int dedo1 { };
	int dedo2 { };
	int dedo3 { };

	std::cin >> dedo1 >> dedo2 >> dedo3;

	int soma { dedo1 + dedo2 + dedo3 };

	if (soma == 0)
		std::cout << "joguem de novo\n";

	else {
		
		if (soma == 1 || soma % 26 == 1)
			std::cout << "a\n";
		else if (soma == 2 || soma % 26 == 2)
			std::cout << "b\n";
		else if (soma == 3 || soma % 26 == 3)
			std::cout << "c\n";
		else if (soma == 4 || soma % 26 == 4)
			std::cout << "d\n";
		else if (soma == 5 || soma % 26 == 5)
			std::cout << "e\n";
		else if (soma == 6 || soma % 26 == 6)
			std::cout << "f\n";
		else if (soma == 7 || soma % 26 == 7)
			std::cout << "g\n";
		else if (soma == 8 || soma % 26 == 8)
			std::cout << "h\n";
		else if (soma == 9 || soma % 26 == 9)
			std::cout << "i\n";
		else if (soma == 10 || soma % 26 == 10)
			std::cout << "j\n";
		else if (soma == 11 || soma % 26 == 11)
			std::cout << "k\n";
		else if (soma == 12 || soma % 26 == 12)
			std::cout << "l\n";
		else if (soma == 13 || soma % 26 == 13)
			std::cout << "m\n";
		else if (soma == 14 || soma % 26 == 14)
			std::cout << "n\n";
		else if (soma == 15 || soma % 26 == 15)
			std::cout << "o\n";
		else if (soma == 16 || soma % 26 == 16)
			std::cout << "p\n";
		else if (soma == 17 || soma % 26 == 17)
			std::cout << "q\n";
		else if (soma == 18 || soma % 26 == 18)
			std::cout << "r\n";
		else if (soma == 19 || soma % 26 == 19)
			std::cout << "s\n";
		else if (soma == 20 || soma % 26 == 20)
			std::cout << "t\n";
		else if (soma == 21 || soma % 26 == 21)
			std::cout << "u\n";
		else if (soma == 22 || soma % 26 == 22)
			std::cout << "v\n";
		else if (soma == 23 || soma % 26 == 23)
			std::cout << "w\n";
		else if (soma == 24 || soma % 26 == 24)
			std::cout << "x\n";
		else if (soma == 25 || soma % 26 == 25)
			std::cout << "y\n";
		else if (soma == 26 || soma % 26 == 0)
			std::cout << "z\n";
	}
}