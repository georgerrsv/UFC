#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

    int value;
    char c;
    vector<int> vet;

    do {
        scanf("%d%c", &value, &c);
        vet.push_back(value);
    }
    while(c != '\n');

    reverse(vet.begin(), vet.end());
    
    int size = vet.size();
    
    cout << "[ ";
    for(int i = 0; i < size; i++) {
        cout << (i == 0 ? "" : " ") << vet[i];
    }
    cout << " ]";
    cout << endl;
}
