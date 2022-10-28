#include <iostream>

int main() {

  int num {};
  int aux {};
  int reverso {};
  
  std::cin >> num;
  aux = num;
  reverso = 0;

  while (aux != 0) {
    reverso = reverso * 10 + aux % 10;
    aux = aux / 10;
  }

  std::cout << (reverso == num ? "1\n" : "0\n");
}