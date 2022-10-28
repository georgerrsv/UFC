#include <iostream>
#include <vector>
#include <aux.hpp> 
using namespace aux;

int count(std::vector<int> vet, int x) {
    
    int aux = 0;
    for(auto elem : vet)
        if(elem == x)
            aux++;
    return aux;
}

int sum(std::vector<int> vet) {
    
    int aux = 0;
    for(int i = 0; i < (int) vet.size(); i++)
        aux += abs(vet[i]);
    return aux;
} 

double average (std::vector<int> vet) {
    
    double value {};
    for (auto elem : vet)
        value += abs(elem);
    return value / vet.size();
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

int main(){
    Chain chain;
    Param ui;

    chain["count"]        = [&] { show <<        count(to_vet<int>(ui[1]), to<int>(ui[2])); };
    chain["sum"]          = [&] { show <<          sum(to_vet<int>(ui[1])                ); };
    chain["average"]      = [&] { show <<      average(to_vet<int>(ui[1])                ); };
    chain["more_men"]     = [&] { show <<     more_men(to_vet<int>(ui[1])                ); };
    chain["half_compare"] = [&] { show << half_compare(to_vet<int>(ui[1])                ); };
    chain["sex_battle"]   = [&] { show <<   sex_battle(to_vet<int>(ui[1])                ); };

    execute(chain, ui);
}
