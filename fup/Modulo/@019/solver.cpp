#include <iostream>

int findPosition(int qtd, int disco, int aviao) {
    if(disco > aviao) {
        int pos = disco - aviao;
        return pos;
    }
    else if(disco < aviao) {
        return qtd / disco;
    }
    else if(disco == aviao) {
        int pos = qtd % aviao + disco;
        return pos;
    }
    return 0;
}

int main() {

	int qtd, disco, aviao;
    std::cin >> qtd >> disco >> aviao;

    std::cout << findPosition(qtd, disco, aviao) << '\n';

}