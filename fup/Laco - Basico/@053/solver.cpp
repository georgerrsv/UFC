#include <iostream>
using namespace std;

int main() {
    
    int h { }; // helicoptero
    int p { }; // policial
    int f { }; // fugitivo
    int d { }; // direcao
    
    std::cin >> h
             >> p
             >> f
             >> d;
    while (!(f == h || f == p)){
        
        f = f + d;
        f = (f + 16) % 16;
    }
    cout << (f == h ? "S\n" : "N\n");
        
}


