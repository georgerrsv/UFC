#include <iostream>
#include <algorithm>
#include <vector>
#include <aux.hpp>
using namespace aux;

bool is(std::vector<int> vet, int value) {
    for(auto elem : vet)
        if(elem == value)
            return true;
    return false;
}

bool back(int x, int y) {
    return abs(x) < abs(y);
}

std::vector<int> get_men (std::vector<int> vet) {
    
    int aux = 0;
    std::vector<int> homem;
    for(int i = 0; i < (int)vet.size(); i++)
        if(vet[i] > 0) {
            aux = vet[i];
            homem.push_back(aux);
        }
    return homem;
} 

std::vector<int> get_calm_women (std::vector<int> vet) {

    int aux = 0;
    std::vector<int> mulher;
    for(int i = 0; i < (int)vet.size(); i++)
        if(vet[i] < 0 && vet[i] > -10) {
            aux = vet[i];
            mulher.push_back(aux);
        }
    return mulher;
} 

std::vector<int> sort (std::vector<int> vet) {

    int aux = 0;
    std::vector<int> absoluto;
    for(int i = 0; i < (int)vet.size(); i++) {
        aux = vet[i];
        absoluto.push_back(aux);
    }
    std::sort(begin(absoluto), end(absoluto));

    return absoluto;
} 

std::vector<int> sort_stress (std::vector<int> vet) {

    int aux = 0;
    std::vector<int> sort_vet;
    for(int i = 0; i < (int)vet.size(); i++)
        if(vet[i] > 0) {
            aux = vet[i];
            sort_vet.push_back(aux);
        }
        else if(vet[i] < 0) {
            aux = vet[i];
            sort_vet.push_back(aux);
        }
    std::sort(sort_vet.begin(), sort_vet.end(), back);

    return sort_vet;
} 

std::vector<int> reverse (std::vector<int> vet) {
    
    int aux = 0;
    std::vector<int> lista_nova;
    for(int i = 0; i < (int)vet.size(); i++)
        if(vet[i] > 0) {
            aux = vet[i];
            lista_nova.push_back(aux);
        }
        else if(vet[i] < 0) {
            aux = vet[i];
            lista_nova.push_back(aux);
        }
    reverse(lista_nova.begin(), lista_nova.end());

    return lista_nova;
} 

std::vector<int> reverse_inplace (std::vector<int> vet) {
    
    int aux = 0;
    std::vector<int> reverso;
    for(int i = 0; i < (int)vet.size(); i++)
        if(vet[i] > 0) {
            aux = vet[i];
            reverso.push_back(aux);
        }
        else if(vet[i] < 0) {
            aux = vet[i];
            reverso.push_back(aux);
        }
    reverse(reverso.begin(), reverso.end());;

    return reverso;
} 

std::vector<int> unique (std::vector<int> vet) {
    
    std::vector<int> unico;
    for(auto elem : vet)
        if(!is(unico, elem))
            unico.push_back(elem);
    return unico;
} 

std::vector<int> repeated(std::vector<int> vet) {

    std::vector<int> unico;
    std::vector<int> repetido;
    for(auto elem : vet)
        if(!is(unico, elem))
            unico.push_back(elem);
        else
            repetido.push_back(elem);
    return repetido;
} 

int main(){
    Chain chain;
    Param ui;

    chain["get_men"]         = [&] { show <<        get_men(to_vet<int>(ui[1])); };
    chain["get_calm_women"]  = [&] { show << get_calm_women(to_vet<int>(ui[1])); };
    chain["sort"]            = [&] { show <<           sort(to_vet<int>(ui[1])); };
    chain["sort_stress"]     = [&] { show <<    sort_stress(to_vet<int>(ui[1])); };
    chain["reverse"]         = [&] { show <<        reverse(to_vet<int>(ui[1])); };
    chain["reverse_inplace"] = [&] { show << reverse_inplace(to_vet<int>(ui[1])); };
    chain["unique"]          = [&] { show <<         unique(to_vet<int>(ui[1])); };
    chain["repeated"]        = [&] { show <<       repeated(to_vet<int>(ui[1])); };

    execute(chain, ui);
}


