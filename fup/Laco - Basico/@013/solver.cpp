#include <iostream>
using namespace std;

int sum_pair(int a, int b) {
    
    int sum = 0;
    
    if (b >= a) {
        for (int i = a; i <= b; i++)
            if (i % 2 == 0)
                if (i % 3 == 0)
                    sum += i;
        return sum;
    }
    else if (b < a)
        return -1;
    return 0;
}

int main() {

    int a, b;

    cin >> a >> b;

    int result = sum_pair(a, b);

    if(sum_pair(a, b) == -1) {
        cout << "invalido" << '\n';
    }
    else
        cout << result << '\n';
}