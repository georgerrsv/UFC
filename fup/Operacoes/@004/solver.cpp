#include <iostream>
#include <math.h>

void distance(float xa, float xb, float ya, float yb) {

	float distancia { sqrt((xb - xa)*(xb - xa) + (yb - ya)*(yb - ya)) };
    printf("%.2f\n", distancia);
}

int main() {

	float xa, xb, ya, yb;
    std::cin >> xa >> ya >> xb >> yb;
	distance(xa, xb, ya, yb);
}