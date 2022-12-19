#include <iostream>

int area_calculator(int comp1, int larg1, int comp2, int larg2) {
	
	int area_1 { comp1 * larg1 };
	int area_2 { comp2 * larg2 };
	return (area_1 > area_2 ? area_1 : area_2);
}

int main() {

	int comp1, larg1, comp2, larg2;

    std::cin >> comp1 >> larg1 >> comp2 >> larg2;

	int calc = area_calculator(comp1, larg1, comp2, larg2);
	
	std::cout << calc << '\n';
}