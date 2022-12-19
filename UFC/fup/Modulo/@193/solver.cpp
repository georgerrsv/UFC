#include <iostream>

int main() {

	int n;

	std::cin >> n;

	int pecas = ((n + 1) * (n + 2) / 2);

	std::cout << pecas << '\n';

}