#include <iostream>

int main() {

	char qt1 { };
	char qt2 { };
	char qt3 { };
	char qt4 { };

	std::cin >> qt1 >> qt2 >> qt3 >> qt4;

	if (qt1 != 'd' && qt2 != 'a' && qt3 != 'c' && qt4 != 'd')
		std::cout << "Nunca assistiu\n";
	else if (qt1 == 'd' && qt2 == 'a' && qt3 == 'c' && qt4 == 'd')
		std::cout << "Super Fa\n";
	else if (qt1 == 'd' && qt2 != 'a' && qt3 != 'c' && qt4 != 'd')
		std::cout << "Ja ouviu falar\n";
	else if (qt1 != 'd' && qt2 == 'a' && qt3 != 'c' && qt4 != 'd')
		std::cout << "Ja ouviu falar\n";
	else if (qt1 != 'd' && qt2 != 'a' && qt3 == 'c' && qt4 != 'd')
		std::cout << "Ja ouviu falar\n";
	else if (qt1 != 'd' && qt2 != 'a' && qt3 != 'c' && qt4 == 'd')
		std::cout << "Ja ouviu falar\n";
	else if (qt1 == 'd' && qt2 == 'a' && qt3 == 'c' && qt4 != 'd')
		std::cout << "Fa\n";
	else if (qt1 != 'd' && qt2 == 'a' && qt3 == 'c' && qt4 == 'd')
		std::cout << "Fa\n";
	else if (qt1 == 'd' && qt2 != 'a' && qt3 == 'c' && qt4 == 'd')
		std::cout << "Fa\n";
	else if (qt1 == 'd' && qt2 == 'a' && qt3 != 'c' && qt4 == 'd')
		std::cout << "Fa\n";
	else if (qt1 == 'd' && qt2 == 'a' && qt3 != 'c' && qt4 != 'd')
		std::cout << "Interessado no assunto\n";
	else if (qt1 == 'd' && qt2 != 'a' && qt3 == 'c' && qt4 != 'd')
		std::cout << "Interessado no assunto\n";
	else if (qt1 == 'd' && qt2 != 'a' && qt3 != 'c' && qt4 == 'd')
		std::cout << "Interessado no assunto\n";
	else if (qt1 != 'd' && qt2 == 'a' && qt3 == 'c' && qt4 != 'd')
		std::cout << "Interessado no assunto\n";
}