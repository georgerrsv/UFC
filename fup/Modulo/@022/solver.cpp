#include <iostream>

int output(int capMax, int qtdAluno) {
    int resto = qtdAluno % (capMax - 1);

    if(resto == 0) {
        qtdAluno = qtdAluno / (capMax - 1);
        return qtdAluno;
    }
    qtdAluno = qtdAluno / (capMax - 1) + 1;
    return qtdAluno;
}

int main() {
	
	int capMax, qtdAluno;
    std::cin >> capMax >> qtdAluno;

    std::cout << output(capMax, qtdAluno) << '\n';

}