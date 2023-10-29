from proxy import *
import time

proxy = Proxy()

print("-----------------------------------")
print("Gerenciador de catálogo de filmes")
print("-----------------------------------")
print("Operações:\n1-Cadastrar\n2-Remover\n3-Listar Detalhes\n4-Exibir catálogo\n5-Sair")
print("-----------------------------------")

while True:
    operation = int(input("Insira uma operação: "))

    if operation == 1:
        proxy.adicionarFilme()
    elif operation == 2:
        proxy.removerFilme()
    elif operation == 3:
        proxy.exibirDetalhe()
    elif operation == 4:
        proxy.mostrarCatalogo()
    elif operation == 5:
        print("Encerrando...")
        time.sleep(1)
        break