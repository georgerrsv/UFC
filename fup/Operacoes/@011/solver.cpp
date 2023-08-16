#include <iostream>

int main() {

	int hora;
	int minuto;
	int dia;
	int mes;
	int ano;

    std::cin >> hora >> minuto >> dia >> mes >> ano;

	int ano_formatado = ano % 100;
		
	printf("%02d:%02d %02d/%02d/%02d\n", hora, minuto, dia, mes, ano_formatado);
}