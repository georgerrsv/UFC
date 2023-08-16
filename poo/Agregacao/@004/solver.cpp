#include <iostream>
#include <sstream>
#include <memory>  //sharedptr
#include <iomanip> //setprecision
#include <utility> //exchange
#include <aux.hpp>

class Lead {
    float thickness;
    std::string hardness;
    int size;

public:
    Lead(float thickness, std::string hardness, int size) {
        this->thickness = thickness;
        this->hardness = hardness;
        this->size = size;
    }

    int usagePerSheet() const {
        if(hardness == "HB")
            return 1;
        if(hardness == "2B")
            return 2;
        if(hardness == "4B")
            return 4;
        return 6;
    }

    float getThickness() const {
        return this->thickness;
    }

    std::string getHardness() const {
        return this->hardness;
    }

    int getSize() const {
        return this->size;
    }

    void setSize(int size) {
        this->size = size;
    }
    std::string str() const {
        std::stringstream ss;
        ss << std::fixed << std::setprecision(1) 
           << thickness << ":" << hardness << ":" << size;
        return ss.str();
    }
};

std::ostream& operator<<(std::ostream& ss, Lead gr) {
    return ss << gr.str();
}

struct Pencil {
    float thickness {0.f};
    std::shared_ptr<Lead> tip {nullptr};

    Pencil(float thickness = 0.0) {
        this->thickness = thickness;
        this->tip = tip;
    }

    bool hasGrafite() {
        if(this->tip != nullptr)
            return true;
        return false;
    }

    bool insert(std::shared_ptr<Lead> grafite) {
        if(this->tip != nullptr) {
            std::cout << "fail: ja existe grafite\n";
            return false;
        }
        if(grafite->getThickness() != this->thickness) {
            std::cout << "fail: calibre incompativel\n";
            return false;
        }
        this->tip = grafite;
        return true;
    }

    std::shared_ptr<Lead> remove() {
        if(this->tip != nullptr) {
            auto rv = this->tip;
            this->tip = nullptr;
            return rv;
        }
        std::cout << "fail: nao existe grafite\n";
        return nullptr;
    }

    void writePage() {
        if(this->tip == nullptr) {
            std::cout << "fail: nao existe grafite\n";
            return;
        }
        auto usage = this->tip->usagePerSheet() * this->tip->getSize();
        if(usage <= this->tip->getSize()) {
            this->tip->setSize(this->tip->getSize() - usage);
            return;
        }
        if(usage > this->tip->getSize()) {
            std::cout << "fail: tamanho insuficiente\n";
            return;
        }
        if(this->tip->getSize() == 0) {
            std::cout << "fail: grafite esgotado\n";
            return;
        }
    }

    std::string str() {
        std::stringstream ss;
        ss << "calibre: " << thickness << ", grafite: ";
        if (tip != nullptr)
            ss << "[" << *tip << "]";
        else
            ss << "null";
        return ss.str();
    }
};

std::ostream& operator<<(std::ostream& os, Pencil l) {
    return os << l.str();
}

int main() {
    aux::Chain chain;
    aux::Param ui;

    Pencil pencil;

    auto tofloat = aux::to<float>;
    auto toint   = aux::to<int>;

    chain["show"]   = [&]() { std::cout << pencil << std::endl; };
    chain["init"]   = [&]() { pencil = Pencil(tofloat(ui[1])); };
    chain["insert"] = [&]() { pencil.insert(std::make_shared<Lead>(tofloat(ui[1]), ui[2], toint(ui[3]))); };
    chain["remove"] = [&]() { pencil.remove(); };
    chain["write"]  = [&]() { pencil.writePage(); };

    aux::execute(chain, ui);
}

