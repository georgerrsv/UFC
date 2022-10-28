#include <iostream>
#include <string>

std::string media(float n1, float n2, float nfinal) {
    float media = (n1 + n2) / 2;
    if(media >= 7) {
        return "aprovado\n";
    }
    else if(media < 7 && media >= 4) {
        float mediaFinal = (media + nfinal) / 2;
        if(mediaFinal >= 5) {
            return "aprovado na final\n";
        }
        else {
            return "reprovado na final\n";
        }
    }
    return "reprovado\n";
}

int main() {

    float n1, n2, nfinal;
    std::cin >> n1 >> n2 >> nfinal;
    std::string result = media(n1, n2, nfinal);
    std::cout << result;
}