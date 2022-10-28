#include <iostream>
using namespace std;

int main() {

	int dimensao, x, y, seg;
	char direcao;

	cin >> dimensao >> x >> y >> direcao >> seg;

	if (direcao == 'R') {
		int pos_x = (x + seg) % dimensao;
		cout << pos_x << " " << y << '\n';
	}
	else if (direcao == 'L') {
		int pos_x = ((x - seg % dimensao) + dimensao) % dimensao;
		cout << pos_x << " " << y << '\n';
	}
	else if (direcao == 'U') {
		int pos_y = (y - seg + dimensao) % dimensao;
		cout << x << " " << pos_y << '\n';
	}
	else if (direcao == 'D') {
		int pos_y = (y + seg) % dimensao;
		cout << x << " " << pos_y << '\n';
	}
}