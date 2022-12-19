#include <iostream>

int main() {
    int hora;
    int min;
    int seg;

    std::cin >> hora >> min >> seg;

    seg += 1;
    
    if (seg == 60) {
        seg = 0;
        min = min + 1;
    }
    if (min == 60) {
        min = 0;
        hora = hora + 1;
    }
    
    if (hora == 24) {
        hora = 0;
    }
    
    printf("%02d %02d %02d\n", hora, min, seg);
}