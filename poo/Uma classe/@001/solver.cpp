#include <iostream>
#include <sstream>
#include <iomanip>

struct Calculator {
    int batteryMax;
    int battery;
    float display;

    Calculator(int batteryMax) {
        this->batteryMax = batteryMax;
        this->battery = 0;
        this->display = 0;
    }

    void chargeBattery(int value) { 
        this->battery += value;
        if (this->battery > this->batteryMax) {
            this->battery = this->batteryMax;
        }
    }

    bool useBattery() {
        if (this->battery > 0) {
            this->battery--;
            return true;
        }
        std::cout << "fail: bateria insuficiente\n";
        return false;
    }

    void sum(int a, int b) { 
        if (this->useBattery()) {
            this->display = a + b;
        }
    }

    void division(int num, int den) {
        if(this->useBattery()) {
            if(den > 0) {
                this->display = (float)num / den;
                return;
            }
            if(den <= 0) {
                std::cout << "fail: divisao por zero\n";
                return;
            }
        }
    }

    std::string str() { 
        std::stringstream ss;
        ss << "display = " << std::fixed << std::setprecision(2) << this->display;
        ss << ", battery = " << this->battery;
        return ss.str();
    }
};

std::ostream& operator<<(std::ostream& os, Calculator c) {
    return (os << c.str());
}

#include <aux.hpp>

int main() {
    Calculator c(0);
    aux::Chain chain;
    aux::Param ui;

    // função para obter um parâmetro convertido para inteiro
    auto par2int   = LAMBDAE(&ui, index, ui.at(index) | aux::STR2<int>());                            //converte de string para int

    chain["show"]   = [&]() { std::cout << c << std::endl;         };
    chain["init"]   = [&]() {  c = Calculator(par2int(1)          ); };
    chain["charge"] = [&]() { c.chargeBattery(par2int(1)          ); };
    chain["sum"]    = [&]() {           c.sum(par2int(1), par2int(2)); };
    chain["div"]    = [&]() {      c.division(par2int(1), par2int(2)); };

    aux::execute(chain, ui);
}

