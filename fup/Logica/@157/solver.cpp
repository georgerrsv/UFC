#include <iostream>
#include <string>

std::string calc(double alc, double gas, double rend_alc, double rend_gas) {
    rend_alc = rend_alc / alc;
    rend_gas = rend_gas / gas;

    if (rend_alc > rend_gas)
        return "A\n";
    else if (rend_alc < rend_gas)
        return "G\n";
    return "G\n";
}

int main() {

	double alc, gas, rend_alc, rend_gas;

	std::cin >> alc >> gas >> rend_alc >> rend_gas;
	
    std::string result = calc(alc, gas, rend_alc, rend_gas);
    std::cout << result;

}