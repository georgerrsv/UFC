#include <iostream>
#include <list>
#include <sstream>
#include <memory>
#include <aux.hpp>

class Kid {
private:
    int age;
    std::string name;
public:
    Kid(std::string name, int age) {
        this->age = age;
        this->name = name;
    }
    int getAge() {
        return this->age;
    }
    std::string getName() {
        return this->name;
    }
    std::string str() {
        return this->name + ":" + std::to_string(this->age);
    }
};

using PtrKid = std::shared_ptr<Kid>;

std::ostream& operator<<(std::ostream& os,  PtrKid kid) {
    return (os << kid->str());
}

class Trampoline {
    std::list<PtrKid> waiting;
    std::list<PtrKid> playing;
    
    PtrKid removeFromList(std::string name, std::list<PtrKid>& lista) {
        if(lista.empty()) {
            return nullptr;
        }
        for(auto it = lista.begin(); it != lista.end(); it++) {
            if((*it)->getName() == name) {
                PtrKid kid = *it;
                lista.erase(it);
                return kid;
            }
        }
        return nullptr;
    }

public:
    Trampoline() {
        this->waiting = std::list<PtrKid>();
        this->playing = std::list<PtrKid>();
    }
    
    void arrive(PtrKid kid) {
        this->waiting.push_back(kid);
    }

    void enter() {
        if(this->waiting.size() > 0) {
            PtrKid kid = this->waiting.front();
            this->waiting.pop_front();
            this->playing.push_back(kid);
        }
    }

    void leave() {
        if(this->playing.size() > 0) {
            PtrKid kid = this->playing.front();
            this->playing.pop_front();
            this->waiting.push_back(kid);
        }
    }

    PtrKid removeKid(std::string name) {
        if(this->playing.size() > 0) {
            PtrKid kid = this->removeFromList(name, this->playing);
            if(kid != nullptr) {
                return kid;
            }
        }
        if(this->waiting.size() > 0) {
            PtrKid kid = this->removeFromList(name, this->waiting);
            if(kid != nullptr) {
                return kid;
            }
        }
        return nullptr; 
    }
    std::string str() {
        return (waiting | aux::FMT()) + " => " + (playing | aux::FMT());
    }
};

int main() {
    aux::Chain chain;
    aux::Param param;
    Trampoline tr;
    chain["arrive"] = [&]() { tr.arrive(std::make_shared<Kid>(param[1], aux::to<int>(param[2]))); };
    chain["enter"]  = [&]() { tr.enter(); };
    chain["leave"]  = [&]() { tr.leave(); };
    chain["remove"] = [&]() { tr.removeKid(param[1]); };
    chain["show"]   = [&]() { std::cout << tr.str() << std::endl; };

    aux::execute(chain, param);
}