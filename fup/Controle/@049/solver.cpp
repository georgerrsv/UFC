#include <iostream>
using namespace std;

int main() {
    
    int fundo_poco { };
    int salto { };
    int escorrega { };
    
    cin >> fundo_poco
        >> salto
        >> escorrega;
        
    int pos { 0 };
        
    while (true) {
        cout << pos;
        pos += salto;
        if (pos >= fundo_poco){
            cout << " saiu\n";
            break;
        }
        cout << " " << pos << "\n";
        pos -= escorrega;
    }
}