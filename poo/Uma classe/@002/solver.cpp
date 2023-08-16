#include <iostream>
#include <sstream>
#include <aux.hpp>

class Car {
public:
    int pass {0};
    int passMax {2};
    int gas {0};
    int gasMax {100};
    int km {0};

    Car() {
    }

    void enter() {
        if(pass == passMax) {
            std::cout << "fail: limite de pessoas atingido\n";
        }
        else {
            pass += 1;
        }
    }

    void leave() {
        if(pass == 0) {
            std::cout << "fail: nao ha ninguem no carro\n";
        }
        else {
            pass -= 1;
        }
    }

    void fuel(int gas) {
        if(gas > gasMax) {
            this->gas = gasMax % gas;
        }
        else {
           this->gas += gas; 
        }
    }

    void drive(int km) {
        if(pass == 0) {
            std::cout << "fail: nao ha ninguem no carro\n";
            return;
        }
        if(gas == 0) {
            std::cout << "fail: tanque vazio\n";
            return;
        }
        if(gas < km) {
            std::cout << "fail: tanque vazio apos andar " << this->gas << " km\n";
            this->km += this->gas;
            this->gas = 0;
            return;
        }
        this->km = km % this->gasMax;
        this->gas -= km;
        
    }

    std::string str() {
       std::stringstream ss;
       ss << "pass: " << pass << ", gas: " << gas << ", km: " << km << "";
       return ss.str();
    }
};

int main() {
    aux::Chain chain;
    aux::Param ui;

    Car car;

    auto par2int   = LAMBDAE(&ui, index, ui.at(index) | aux::STR2<int>()); //converte de string para int

    chain["show"]  = [&](){ car.str() | aux::PRINT(); };
    chain["enter"] = [&](){ car.enter(); };
    chain["leave"] = [&](){ car.leave(); };
    chain["fuel"]  = [&](){ car.fuel(par2int(1)); };
    chain["drive"] = [&](){car.drive(par2int(1)); };

    aux::execute(chain, ui);
}
