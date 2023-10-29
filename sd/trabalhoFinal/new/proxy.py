from udpClient import UDPClient
from json import *
from filme import Filme
from cabecalho import Cabecalho

class Proxy:
    def __init__(self):
        self.client = UDPClient('localhost', 8080)

    def adicionarFilme(self):
        print("[Cadastrar]")
        titulo = input("Titulo: ")
        diretor = input("Diretor: ")
        ano = int(input("Ano: "))
        duracao = float(input("Duração: "))
        genero = input("Gênero: ")
        classificacao = input("Classificação: ")
        descricao = input("Descrição: ")

        filme = Filme(titulo, diretor, ano, duracao, genero, classificacao, descricao)
        filme_json = filme.to_json()
        cabecalho = Cabecalho(0, "adicionarFilme", 1, {"filme": filme_json})
        h_json = cabecalho.to_json()
        self.client.sendRequest(h_json)
        data = self.client.getResponse()
        header = Cabecalho.from_json(data)
        print(header.arguments)

    def removerFilme(self):
        print("[Remover]")
        id = int(input("ID: "))
        cabecalho = Cabecalho(0, "removerFilme", 2, {"id": id})
        h_json = cabecalho.to_json()
        self.client.sendRequest(h_json)
        data = self.client.getResponse()
        header = Cabecalho.from_json(data)
        print(header.arguments)

    def exibirDetalhe(self):
        print("[Exibir detalhe]")
        id = int(input("ID: "))
        cabecalho = Cabecalho(0, "exibirDetalhe", 3, {"id": id})
        h_json = cabecalho.to_json()
        self.client.sendRequest(h_json)
        data = self.client.getResponse()
        header = Cabecalho.from_json(data)
        print(header.arguments)

    def mostrarCatalogo(self):
        print("[Exibir catálogo]")
        cabecalho = Cabecalho(0, "mostrarCatalogo", 4, "")
        h_json = cabecalho.to_json()

        self.client.sendRequest(h_json)
        data = self.client.getResponse()
        header = Cabecalho.from_json(data)

        if "Catalogo vazio!" in header.arguments:
            print("Catálogo vazio!")
        else:
            for filme in header.arguments:
                print(filme)