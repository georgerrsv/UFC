#include <iostream>
#include <vector>
#include <sstream>
#include <memory>
#include <sstream>
#include <aux.hpp>

struct Cliente{
    std::string id;
    std::string fone;

    Cliente(std::string id = "", std::string fone = "") {
        this->id = id;
        this->fone = fone;
    }

    std::string str() {
        std::stringstream ss;
        ss << this->id << ":" << this->fone;
        return ss.str();
    }

    std::string getFone() {
        return this->fone;
    }

    std::string getId() {
        return this->id;
    }
};

using PtrCliente = std::shared_ptr<Cliente>;

std::ostream& operator<<(std::ostream& os, Cliente c) {
    return os << c.str();
}

class Sala{
    std::vector<PtrCliente> cadeiras;

    int procurar(std::string nome) {
        for(auto i = 0u; i < cadeiras.size(); i++) {
            if(cadeiras[i]->getId() == nome) {
                return i;
            }
        }
        return -1;
    }

    bool verificarIndice(int pos) {
        return pos >= 0 && pos < (int)cadeiras.size();
    }

public:
    Sala(int qtd = 0) {
        this->cadeiras = std::vector<PtrCliente>(qtd, nullptr);
    }


    void reservar(std::string id, std::string fone, int ind) {
        if(verificarIndice(ind) && cadeiras[ind] == nullptr) {
            cadeiras[ind] = std::make_shared<Cliente>(id, fone);
            return;
        }
        if(verificarIndice(ind) && cadeiras[ind] != nullptr) {
            std::cout << "fail: cadeira ja esta ocupada\n";
            return;
        }
        if(!verificarIndice(ind)) {
            std::cout << "fail: cadeira nao existe\n";
            return;
        }
    }

    void cancelar(std::string id) {
        int ind = procurar(id);
        cadeiras[ind] = nullptr;
    }

    std::string str() {
        std::string receive = "";
        for(int i = 0; i < (int)cadeiras.size(); i++) {
            if(cadeiras[i] != nullptr) {
                if(i == (int)cadeiras.size() - 1) {
                    receive += cadeiras[i]->str();
                } else {
                    receive += cadeiras[i]->str() + " ";
                }
            }
            if(cadeiras[i] == nullptr) {
                if(i == (int)cadeiras.size() - 1) {
                    receive += "-";
                } else {
                    receive += "- ";
                }
            }
        }
        return "[" + receive + "]";
    }
};

int main() {
    aux::Chain chain;
    aux::Param param;
    Sala sala;
    chain["init"]     = [&]() { sala = Sala(aux::to<int>(param[1])); };
    chain["reservar"] = [&]() { sala.reservar(param[1], param[2], aux::to<int>(param[3])); };
    chain["cancelar"] = [&]() { sala.cancelar(param[1]); };
    chain["show"]     = [&]() { std::cout << sala.str() << std::endl; };
    aux::execute(chain, param);
}

