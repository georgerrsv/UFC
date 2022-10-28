#include <iostream>

int output(int cap, int banana, int goiaba, int manga) {
    int total = banana + goiaba + manga;
    if(cap < total && total % cap == 2) {
        total = total % cap;
        return total;
    }
    else if(cap < total && total % cap >= 1) {
        return (total/cap) + 1;
    }
    else if(cap > total) {
        return cap / total;
    }
    else if(cap < total && total % cap == 0) {
        return total / cap;
    }
    return total / cap;
}

int main() {

    int cap, banana, goiaba, manga;
    std::cin >> cap >> banana >> goiaba >> manga;

    std::cout << output(cap, banana, goiaba, manga) << '\n';

}