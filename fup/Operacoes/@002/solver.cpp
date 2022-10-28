#include <iostream>
#include <math.h>

void area_do_triangulo(float lado_a, float lado_b, float lado_c) {

	float perimetro{ (lado_a + lado_b + lado_c) / 2 };
	float area = sqrt(perimetro * (perimetro - lado_a) * (perimetro - lado_b) * (perimetro - lado_c));
    printf("%.2f\n", area);
}

int main() {

	float a, b, c;
    std::cin >> a >> b >> c;

	area_do_triangulo(a, b, c);
}