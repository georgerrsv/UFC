#include <iostream>

int calculator(int num1, int num2, char op) {

	if (op == '+') {
		int sum = num1 + num2;
		return sum;
	}
	else if (op == '-') {
		int sub = num1 - num2;
		return sub;
	}
	else if (op == '/') {
		int div = num1 / num2;
		return div;
	}
	else if (op == '*') {
		int mult = num1 * num2;
		return mult;
	}
	return 0;
}

int main() {

	int num1, num2;
	char op;
    std::cin >> num1 >> num2 >> op;

	int result = calculator(num1, num2, op);
	std::cout << result << '\n';
}