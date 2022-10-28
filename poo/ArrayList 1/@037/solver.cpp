#include <iostream>
#include <memory>
#include <vector>
#include <list>
#include <string>
#include <utility>
#include <aux.hpp>


class Pessoa {
    std::string nome;
public:
    Pessoa(std::string nome) {
        this->nome = nome;
    }
    std::string getNome() const {
        return this->nome; 
    }
    std::string str() const {
        return this->nome;
    }
};
std::ostream& operator<<(std::ostream& os, const Pessoa& p) {
    return (os << p.str());
}

class Mercantil {
    std::vector<std::shared_ptr<Pessoa>> caixas; //caixas do supermercado
    std::list  <std::shared_ptr<Pessoa>> esperando; //lista de clientes esperando

    bool validarIndice(int indice) {
        if(indice < 0 || indice >= (int)this->caixas.size())
            return false;
        return true;
    }

public:
    Mercantil(int qtd_caixas): caixas(qtd_caixas, nullptr) {
    }
    
    void chegar(const std::shared_ptr<Pessoa>& person) {
        this->esperando.push_back(person);
    }

    bool chamarNoCaixa(int indice) {
        if(indice < 0 || indice >= (int)this->caixas.size()) {
            std::cout << "fail: caixa invalido\n";
            return false;
        }
        if(this->caixas[indice] != nullptr) {
            std::cout << "fail: caixa ocupado\n";
            return false;
        }
        if(this->esperando.empty()) {
            std::cout << "fail: sem clientes\n";
            return false;
        }
        auto p_fila = this->esperando.begin();
        this->caixas[indice] = *p_fila;
        this->esperando.erase(p_fila);
        return true;
    }
    
    std::shared_ptr<Pessoa> finalizar(int indice) {
        this->caixas[indice] = nullptr;
        return this->caixas[indice];
    }

    std::string str() const {
        int i = 0;
        auto fn = [&i](auto p) {
            std::stringstream ss; 
            ss << " " << i++ << ":" << (p == nullptr ? "-----" : p->getNome()) << " ";
            return ss.str();
        };
        std::stringstream os;
        os  << "Caixas: |" << (caixas | aux::MAP(fn) | aux::JOIN("|")) << "|\n"
            << "Espera: " << (esperando | aux::MAP(LAMBDA(x, *x)) | aux::FMT());
        return os.str();
    }
};

std::ostream& operator<<(std::ostream& os, const Mercantil& b) {
    return (os << b.str());
}

int main() {
    aux::Chain chain;
    aux::Param par;
    
    Mercantil bank(0);

    chain["init"]   = [&]() {   bank = Mercantil(aux::to<int>(par[1])); };
    chain["call"]   = [&]() { bank.chamarNoCaixa(aux::to<int>(par[1])); };
    chain["finish"] = [&]() {     bank.finalizar(aux::to<int>(par[1])); };
    chain["arrive"] = [&]() { bank.chegar(std::make_shared<Pessoa>(par[1])); };
    chain["show"]   = [&]() { std::cout << bank << '\n'; };

    aux::execute(chain, par);    
}


