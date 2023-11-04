from proxy import Proxy
from filme import Filme
import time
from os import system

proxy = Proxy()

print("-----------------------------------")
print("Gerenciador de catálogo de filmes")
print("-----------------------------------")
print("Operações:\n1-Cadastrar\n2-Remover\n3-Listar Detalhes\n4-Exibir catálogo\n5-Limpar tela\n6-Sair")
print("-----------------------------------")
while True:

    operation = int(input("Insira uma operação: "))

    if operation == 1:
        print("[Cadastrar]")
        titulo = input("Titulo: ")
        diretor = input("Diretor: ")
        ano = input("Ano: ")
        duracao = input("Duração: ")
        genero = input("Gênero: ")
        classificacao = input("Classificação: ")
        descricao = input("Descrição: ")
        filme = Filme(titulo, diretor, ano, duracao, genero, classificacao, descricao)
        proxy.adicionarFilme(filme)

    elif operation == 2:
        print("[Remover]")
        id = input("ID: ")
        proxy.removerFilme(id)

    elif operation == 3:
        print("[Exibindo detalhes]")
        id = input("ID: ")
        proxy.exibirDetalhe(id)

    elif operation == 4:
        print("[Exibir catálogo]")
        proxy.mostrarCatalogo()
    elif operation == 5:
        system("clear")
        print("-----------------------------------")
        print("Gerenciador de catálogo de filmes")
        print("-----------------------------------")
        print("Operações:\n1-Cadastrar\n2-Remover\n3-Listar Detalhes\n4-Exibir catálogo\n5-Limpar tela\n6-Sair")
        print("-----------------------------------")
    elif operation == 6:
        print("Encerrando...")
        time.sleep(1)
        break
    else:
        print("Operação inválida!")
        continue