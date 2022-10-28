#include <iostream>

int odd(int n) {
    
    int primo = 0;
    for(int i = 1; i <= n; i++) {
        if(n % i == 0) {
            primo++;
        }
    }
    if(primo == 2)
        return 1;
    return 0;
}


int main() {

    int n;
    std::cin >> n;
    int result = odd(n);
    std::cout << result << '\n';
}