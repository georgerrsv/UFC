#include <iostream>
#include <vector>
#include <sstream>
#include <iomanip>

bool in (std::vector<int> vet, int value) {
    
    for (auto elem : vet)
        if (elem == value)
            return true;
    return false;
}

double average (std::vector<int> vet) {
    
    double value {};
    for (auto elem : vet)
        value += abs(elem);
    return value / vet.size();
}

int find_if (std::vector<int> vet) {
    
    for (int i = 0; i < (int) vet.size(); i++)
        if (vet[i] > 0)
            return i;
    return -1;

}

int index_of (std::vector<int> vet, int value) {
    
    for (int i = 0; i < (int) vet.size(); i++)
        if (vet[i] == value)
            return i;
    return -1;
}

int min_element (std::vector<int> vet) {

    int pos = -1;
    for (int i = 0; i < (int) vet.size(); i++)
        if (vet[i] < vet[pos])
            pos = i;
    return pos;
}

int find_min_dif (std::vector<int> vet) {

    int menor = vet[0];
    int pos = -1;
    for (int i = 0; i < (int) vet.size(); i++) {
        if (vet[i] > 0) {
            if (vet[i] < menor)
                pos = i;
        }
    }
    return pos;
}

int counter (std::vector<int> vet, int value) {

    int aux = 0;
    for (int i = 0; i < (int) vet.size(); i++) {
        if(vet[i] == value)
            aux++;
    }
    return aux;
}

std::string more_men (std::vector<int> vet) {

    int neg = 0, pos = 0;
    for (int i = 0; i < (int) vet.size(); i++) 
        if (vet[i] < 0)
            neg++;
        else if(vet[i] > 0)
            pos++;
    
    if (pos == neg)
        return "draw";
    else if (pos > neg)
        return "men";
    else
        return "women";
}

float media (std::vector<int> vet, int inicio, int fim) {
    float acc = 0;
    for(int i = inicio; i < fim; i++)
        acc += abs(vet[i]);
    return acc / (fim - inicio);
}

std::string half_compare (std::vector<int> vet) {

    int size = vet.size();
    float first = media(vet, 0, size / 2);
    float meio = size / 2;
    if (size % 2 == 1)
        meio += 1;
    float second = media(vet, meio, size);

    if (first == second)
        return "draw";
    else if (first > second)
        return "first";
    else
        return "second";
}

std::string sex_battle(std::vector<int> vet) {

    int aux = 0;
    float homem = 0, mulher = 0;
    std::vector<int> h;
    std::vector<int> m;

    for(int i = 0; i < (int) vet.size(); i++) {
        if(vet[i] < 0) {
            aux = vet[i];
            m.push_back(aux);
        }
        else if(vet[i] > 0) {
            aux = vet[i];
            h.push_back(aux);
        }
    }

    for(int i = 0; i < (int) h.size(); i++)
        homem += abs(vet[i]);
    for(int i = 0; i < (int) m.size(); i++)
        mulher += abs(vet[i]);

    if (mulher > homem)
        return "women";
    else if (homem > mulher)
        return "men";
    else
        return "draw";
}

std::vector<std::string> split(std::string texto, char sep) {
    std::stringstream ss(texto);
    std::string token {};
    std::vector<std::string> vet;
    while(getline(ss, token, sep))
        vet.push_back(token);
    return vet;
}
template <typename T>
T to(std::string data) {
    T value {};
    std::stringstream(data) >> value;
    return value;    
}

std::vector<int> to_vet(std::string data) {
    std::vector<int> vet;
    for (auto elem : split(data.substr(1, data.size() - 2), ','))
        vet.push_back(to<int>(elem));
    return vet;
}

std::string fmt(std::vector<int> vet) {
    std::stringstream ss;
    ss << "[";
    for(int i = 0; i < (int) vet.size(); i++)
        ss << (i != 0 ? "," : "") << vet[i];
    ss << "]";
    return ss.str();
}

std::string fmt(bool value) {
    return value ? "true" : "false";
}

std::string fmt(double value) {
    std::stringstream ss;
    ss << std::fixed << std::setprecision(2) << value;
    return ss.str();
}
int main() {
    while (true) {
        std::string line {};
        std::getline(std::cin, line); //ler a linha
        std::cout << '$' << line << '\n';
        auto ui = split(line, ' ');   //quebrar em uma lista de palavras
        auto cmd = ui[0];

        if (cmd == "end") {
            break;
        } else if (cmd == "in") {// in [1,2,3] 4
            std::cout << fmt(in(to_vet(ui[1]), to<int>(ui[2]))) << '\n';
        } else if (cmd == "average") {
            std::cout << fmt(average(to_vet(ui[1]))) << '\n';
        } else if (cmd == "find_if") {
            std::cout << find_if(to_vet(ui[1])) << '\n';
        } else if (cmd == "index_of") {
            std::cout << index_of(to_vet(ui[1]), to<int>(ui[2])) << '\n';
        } else if (cmd == "min_element") {
            std::cout << min_element(to_vet(ui[1])) << '\n';
        } else if (cmd == "find_min_if") {
            std::cout << find_min_dif(to_vet(ui[1])) << '\n';
        } else if (cmd == "count") {
            std::cout << counter(to_vet(ui[1]), to<int>(ui[2])) << '\n';
        } else if (cmd == "more_men") {
            std::cout << more_men(to_vet(ui[1])) << '\n';
        } else if (cmd == "half_compare") {
            std::cout << half_compare(to_vet(ui[1])) << '\n';
        } else if (cmd == "sex_battle") {
            std::cout << sex_battle(to_vet(ui[1])) << '\n';
        } else {            
            std::cout << "fail: comando invalido\n";
        }
    }
}
