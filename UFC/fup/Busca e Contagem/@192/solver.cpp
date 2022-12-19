#include <iostream>

int main() {
	
	int monica { };
	int filho1 { };
	int filho2 { };

	std::cin >> monica >> filho1 >> filho2;

	int filho3 = monica - (filho1 + filho2);

	if (filho1 > filho2 && filho1 > filho3)
		std::cout << filho1 << '\n';
	else if (filho2 > filho1 && filho2 > filho3)
		std::cout << filho2 << '\n';
	else if (filho3 > filho1 && filho3 > filho2)
		std::cout << filho3 << '\n';
}