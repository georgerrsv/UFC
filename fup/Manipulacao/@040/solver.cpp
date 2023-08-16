#include <iostream>
#include <string>

std::string trabalhando(int dia, int hora) {
    if(dia != 1 && dia < 7) {
        if(hora >= 8 && hora < 12 || hora >= 14 && hora < 18)
            return "SIM\n";
    }
    else if(dia == 7) {
        if(hora >= 8 && hora < 12)
            return "SIM\n";
    }
    return "NAO\n";
}

int main() {

    int dia, hora, minuto;
    std::cin >> dia >> hora >> minuto;
    std::string result = trabalhando(dia, hora);
    std::cout << result;
}