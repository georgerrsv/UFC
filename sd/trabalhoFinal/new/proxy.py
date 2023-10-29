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
        cabecalho = Cabecalho(0, "cadastrar", 1, {"filme": filme_json})
        h_json = cabecalho.to_json()
        self.client.sendRequest(h_json)
        data = self.client.getResponse()
        header = Cabecalho.from_json(data)
        print(header.arguments)

    def removerFilme(self):
        print("[Remover]")
        id = int(input("ID: "))
        cabecalho = Cabecalho(0, "remover", 2, {"id": id})
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
        header = Cabecalho(0, "mostrarCatalogo", 4, "")
        h_json = header.to_json()

        self.client.sendRequest(h_json)
        data = self.client.getResponse()
        if data:
            header = Cabecalho.from_json(data)
            catalogo = loads(header.arguments)
            for filme_data in catalogo:
                filme = Filme.from_json(filme_data)
                print(filme.to_json())
