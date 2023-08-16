#include <iostream>

int main() {

	float nota1{ };
	float nota2{ };
	float nota3{ };
	float trab{ };

	std::cin >> nota1 >> nota2 >> nota3 >> trab;

	if (nota1 <= nota2 && nota3 < nota2) {

		float media{ (nota1 + nota2 + trab) / 3 };

		if (media >= 7) {
			printf("Aprovado com %.1f\n", media);
		}
		else {
			printf("Final com %.1f\n", media);
		}
	}
	else if (nota1 < nota2 && nota2 >= nota3) {

		float media{ (nota2 + nota3 + trab) / 3 };

		if (media >= 7) {
			printf("Aprovado com %.1f\n", media);
		}
		else {
			printf("Final com %.1f\n", media);
		}
	}
	else if (nota2 < nota1 && nota1 >= nota3) {

		float media{ (nota1 + nota3 + trab) / 3 };

		if (media >= 7) {
			printf("Aprovado com %.1f\n", media);
		}
		else {
			printf("Final com %.1f\n", media);
		}

	}
	else if (nota1 == nota2 && nota2 == nota3) {

		float media{ (nota1 + nota2 + nota3 + trab) / 4 };

		if (media >= 7) {
			printf("Aprovado com %.1f\n", media);
		}
		else {
			printf("Final com %.1f\n", media);
		}
	}

}