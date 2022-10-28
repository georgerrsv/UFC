#include <iostream>

int aumentar_salario(float salario_atual) {

    if(salario_atual <= 1000)
	    return printf("%.2f\n", salario_atual + (salario_atual * 0.20));

	else if(salario_atual > 1000 && salario_atual <= 1500)
		return printf("%.2f\n", salario_atual + (salario_atual * 0.15));

	else if(salario_atual > 1500 && salario_atual <= 2000)
		return printf("%.2f\n", salario_atual + (salario_atual * 0.10));

	else
		return printf("%.2f\n", salario_atual + (salario_atual * 0.05));
	return 0;
}

int main() {

	float salario_atual {};

	std::cin >> salario_atual;
	aumentar_salario(salario_atual);
}