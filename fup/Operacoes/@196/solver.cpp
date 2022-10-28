#include <iostream>

void qtd_parcelas(int valor_tv, int parcela) {

    if(parcela == 1) {
        double valor = (double)valor_tv;
        printf("%.2f\n%.2f\n", valor, valor);
    }
    else if(parcela == 2) {
        double juros { valor_tv * 0.05 };
        double novo_valor { valor_tv + juros };
        double parcela_nova { novo_valor / 2 };
        printf("%.2f\n%.2f\n", parcela_nova, novo_valor);
    }
    else if(parcela == 3) {
        double juros { valor_tv * 0.1 };
        double novo_valor { valor_tv + juros };
        double parcela_nova { novo_valor / 3 };
        printf("%.2f\n%.2f\n", parcela_nova, novo_valor);
    }
    else if(parcela == 4) {
        double juros { valor_tv * 0.15 };
        double novo_valor { valor_tv + juros };
        double parcela_nova { novo_valor / 4 };
        printf("%.2f\n%.2f\n", parcela_nova, novo_valor);
    }
    else if(parcela == 5) {
        double juros { valor_tv * 0.2 };
        double novo_valor { valor_tv + juros };
        double parcela_nova { novo_valor / 5 };
        printf("%.2f\n%.2f\n", parcela_nova, novo_valor);
    }
    else if(parcela == 6) {
        double juros { valor_tv * 0.25 };
        double novo_valor { valor_tv + juros };
        double parcela_nova { novo_valor / 6 };
        printf("%.2f\n%.2f\n", parcela_nova, novo_valor);
    }
    else if(parcela == 7) {
        double juros { valor_tv * 0.3 };
        double novo_valor { valor_tv + juros };
        double parcela_nova { novo_valor / 7 };
        printf("%.2f\n%.2f\n", parcela_nova, novo_valor);
    }
    else if(parcela == 8) {
        double juros { valor_tv * 0.35 };
        double novo_valor { valor_tv + juros };
        double parcela_nova { novo_valor / 8 };
        printf("%.2f\n%.2f\n", parcela_nova, novo_valor);
    }
    else if(parcela == 9) {
        double juros { valor_tv * 0.4 };
        double novo_valor { valor_tv + juros };
        double parcela_nova { novo_valor / 9 };
        printf("%.2f\n%.2f\n", parcela_nova, novo_valor);
    }
    else if(parcela == 10) {
        double juros { valor_tv * 0.45 };
        double novo_valor { valor_tv + juros };
        double parcela_nova { novo_valor / 10 };
        printf("%.2f\n%.2f\n", parcela_nova, novo_valor);
    }
}

int main() {

    int valor_tv, parcela;
    std::cin >> valor_tv >> parcela;
    qtd_parcelas(valor_tv, parcela);
}