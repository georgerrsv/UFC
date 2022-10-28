#include <iostream>
#include <list>
#include <memory>
#include <sstream>
#include <utility>
#include <iomanip> //setprecision
#include <aux.hpp>

class Grafite{
    float calibre;
    std::string dureza;
    int tamanho;
public:
    Grafite(float calibre, std::string dureza, int tamanho) {
        this->calibre = calibre;
        this->dureza = dureza;
        this->tamanho = tamanho;
    }
    int desgastePorFolha() {
        if (dureza == "HB")
            return 1;
        if (dureza == "2B")
            return 2;
        if (dureza == "4B")
            return 4;
        return 6;
    }
    float getCalibre() {
        return this->calibre;
    }
    std::string getDureza() {
        return this->dureza;
    }
    int getTamanho() {
        return this->tamanho;
    }
    void setTamanho(int tamanho) {
        this->tamanho = tamanho;
    }
    std::string str() const {
        std::ostringstream os;
        os << std::fixed << std::setprecision(1) << calibre << ":" << dureza << ":" << tamanho;
        return os.str();
    }
};
std::ostream& operator<<(std::ostream& os, Grafite g) {
    return os << g.str();
}

using PGrafite = std::shared_ptr<Grafite>;

std::ostream& operator<<(std::ostream& os, PGrafite g) {
    return os << "[" << (g == nullptr ? "" : g->str()) << "]";
}

struct Lapiseira{
    float calibre {0.f};
    PGrafite grafite {nullptr};
    std::list<PGrafite> tambor;

    Lapiseira(float calibre = 0.0) {
        this->calibre = calibre;
        
    }

    bool inserir(PGrafite grafite) {
        if(grafite->getCalibre() != this->calibre) {
            std::cout << "fail: calibre incompatível\n";
            return false;
        }
        if(grafite->getCalibre() == this->calibre) {
            if(this->grafite == nullptr) {
                tambor.push_back(grafite);
            }
        }
        return false;
    }

    PGrafite remover() {
        if(this->grafite == nullptr) {
            tambor.push_front(this->grafite);
            this->grafite = nullptr;
        }
        return nullptr;
    }

    void write() {
    }
    void puxar() {
        if(tambor.size() > 0) {
            grafite = tambor.front();
            tambor.pop_front();
        }
        if(tambor.size() == 0) {
            std::cout << "fail: ja existe grafite no bico\n";
            grafite = nullptr;
        }
    }

    std::string str() const {
        std::ostringstream os;
        os << "calibre: " << calibre 
           << ", bico: " << grafite
           << ", tambor: {" << (tambor | aux::JOIN("")) << "}";
        return os.str();
    }
};

std::ostream& operator<<(std::ostream& os, const Lapiseira& l) {
    return os << l.str();
}

int main() {
    aux::Chain chain;
    aux::Param param;
    Lapiseira lapiseira;

    auto FLOAT = [&param](int index) {return aux::to<float>(param[index]);};
    auto __INT = [&param](int index) {return aux::to<int>(param[index]);};

    chain["init"]   = [&]() { lapiseira = Lapiseira(FLOAT(1)); };
    chain["show"]   = [&]() { std::cout << lapiseira << std::endl; };
    chain["insert"] = [&]() { lapiseira.inserir(std::make_shared<Grafite>(FLOAT(1), param[2], __INT(3))); };
    chain["remove"] = [&]() { lapiseira.remover(); };
    chain["pull"]   = [&]() { lapiseira.puxar(); };
    chain["write"]  = [&]() { lapiseira.write(); };

    aux::execute(chain, param);
}

