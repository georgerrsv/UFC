#include <iostream>
#include <memory>
#include <sstream>

enum Ticket { LEVE, MEDIA, GRAVE, GRAVISSIMA };

class Multa {
    float price; // Preço da multa
    std::string type; // Tipo da multa
    int points; // Pontos na carteira
public:
    Multa(Ticket t) {
        switch(t) {
            case LEVE: price = 88; points = 3; type = "leve"; break;
            case MEDIA: price = 130; points = 4; type = "media"; break;
            case GRAVE: price = 195; points = 5; type = "grave"; break;
            case GRAVISSIMA: price = 293; points = 7; type = "gravissima"; break;
        }
    }
    
    Multa(float price, Ticket type, int points) {
        this->price = price;
        this->type = type;
        this->points = points;
    }

    float getPrice() const { 
        return this->price;
    }

    std::string getType() const { 
        return this->type;
    }

    int getPoints() const { 
        return this->points;
    }
};

class Highway {
private:
    int speedLimit; //velocidade permitida em km/h
    int officers = 0; //!= 0 tem fiscalizacao 
public:
    Highway(int speedLimit, int officers) {
        this->speedLimit = speedLimit;
        this->officers = officers;
    }

    int getSpeedLimit() const { 
        return this->speedLimit; 
    }

    void setSpeedLimit(int speed) { 
        this->speedLimit = speed; 
    }

    int getOfficers() const { 
        return this->officers; 
    }

    void setOfficers(int officers) { 
        this->officers = officers; 
    }
};

class Radar : public Highway {
private:
    bool hasRadar {false}; //true se tem radar
    std::string type; //tipo da multa
    int points; //pontos na carteira
    int price; //preço da multa
public:
    Radar(int points, int price, std::string type) : Highway(130, 2) {
        this->points = points;
        this->price = price;
        this->type = type;
    }

    int getPoints() const { 
        return this->points; 
    }

    void setPoints(Multa p) { 
        this->points = p.getPoints(); 
    }

    int getPrice() const { 
        return this->price; 
    }

    void setPrice(Multa pr)  { 
        this->price += pr.getPrice(); 
    }
    
    std::string getType() const { 
        return this->type; 
    }

    void setType(Multa t) { 
        this->type = t.getType(); 
    }

    bool setRadar() {
        if(this->getOfficers() < 0) {
            this->hasRadar = true;
            return true;
        }
        return false;
    }
};

class Vehicle : public Highway {
private:
    int capacity; //capacidade do veículo
    int capacityMax; //capacidade máxima do veículo
    std::string type; //tipo do veículo
    std::string name; //nome do veículo
    std::string index; //placa do veículo
    int year; //ano do veículo
public:
    Vehicle(std::string type, std::string name, std::string index, int year, int capacity, int capacityMax) : Highway(130, 2) {
        this->type = type;
        this->name = name;
        this->index = index;
        this->year = year;
        this->capacity = capacity;
        this->capacityMax = capacityMax;
    }

    int getCapacity() const { 
        return this->capacity; 
    }

    void setCapacity(int capacity) { 
        this->capacity = capacity; 
    }

    std::string getType() const { 
        return this->type; 
    }

    std::string getName() const { 
        return this->name; 
    }

    std::string getIndex() const { 
        return this->index; 
    }

    int getYear() const { 
        return this->year; 
    }

    void setYear(int year) { 
        this->year = year; 
    }

    void setIndex(std::string index) { 
        this->index = index; 
    }

    void setName(std::string name) { 
        this->name = name; 
    }

    void setType(std::string type) { 
        this->type = type; 
    }
};

class Car : public Vehicle {
private:
    int type; //tipo de carro
    std::string index; //placa
    std::string model; //modelo
    int year; //ano
    int speedMax; //velocidade maxima

public:

    Car(std::string index, std::string model, int year, int speedMax) : Vehicle("Carro", "Fusca", index, year, 2, 4) {
        this->index = index;
        this->model = model;
        this->year = year;
        this->speedMax = speedMax;
    }

    std::string getIndex() const { 
        return this->index; 
    }

    std::string getModel() const { 
        return this->model; 
    }

    int getYear() const { 
        return this->year; 
    }

    int getSpeedMax() const { 
        return this->speedMax; 
    }

    void setIndex(std::string index) { 
        this->index = index; 
    }

    void setModel(std::string model) { 
        this->model = model; 
    }

    void setYear(int year) { 
        this->year = year; 
    }

    void setSpeedMax(int speedMax) { 
        this->speedMax = speedMax; 
    }

    std::string str () const {
        std::ostringstream oss;
        oss << "Carro: " << this->getModel() << '\n'
            << "Placa: " << this->getIndex() << '\n'
            << "Ano: " << this->getYear() << '\n'
            << "Velocidade maxima: " << this->getSpeedMax() << '\n'
            << "Capacidade: " << this->getCapacity() << '\n';
        return oss.str();
    }
    
    void getTicket(int speed, Multa m) {
        if(Highway::getOfficers() == 0) {
            std::cout << "Fiscalizacao eletronica ativa\n";
            std::cout << "Velocidade maxima permitida: " << Highway::getSpeedLimit() << "km/h\n";
            std::cout << std::endl;
        }
        if(Highway::getOfficers() > 0) {
            std::cout << "Fiscalizacao ativa. Evite multas, respeite a sinalizacao!\n";
            std::cout << "Velocidade maxima permitida: " << Highway::getSpeedLimit() << "km/h\n";
            std::cout << std::endl;
        }
        if(speed == Highway::getSpeedLimit()) {
            std::cout << "Velocidade limite atingida. Reduza ou sera multado!\n";
            std::cout << std::endl;
        }
        if(speed > Highway::getSpeedLimit()) {
            std::cout << "Multa aplicada por excesso de velocidade!\n";
            std::cout << "Velocidade acima do limite: " << speed - Highway::getSpeedLimit() << "km/h\n";
            std::cout << "Pontos na carteira: " << m.getPoints() << '\n';
            std::cout << "Preco da multa: " << m.getPrice() << '\n';
            std::cout << "Tipo da multa: " << m.getType() << '\n';
            std::cout << std::endl;
            return;
        }
    }
};

int main() {
    Multa m(GRAVISSIMA);
    Car c("XYZ-0123", "McLaren", 2002, 380);
    c.getTicket(220, m);
    std::cout << c.str();
}

