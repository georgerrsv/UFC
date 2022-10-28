#include <iostream>
using namespace std;

string idade(int num) {
    if (num < 12)
        return " eh crianca\n";
    else if (num < 18)
        return " eh jovem\n";
    else if (num < 65)
        return " eh adulto\n";
    else if (num < 1000)
        return " eh idoso\n";
    return " eh mumia\n";
}

int main() {
    
    int value;
    string nome;
    cin >> nome >> value;

    string result = idade(value);
    cout << nome << result;
}