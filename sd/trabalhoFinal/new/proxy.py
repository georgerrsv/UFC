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
        new_request_id = Cabecalho.increment_request_id()
        cabecalho = Cabecalho(0, "adicionarFilme", 1, {"filme": filme_json}, new_request_id)
        h_json = cabecalho.to_json()
        self.client.sendRequest(h_json)
        data = self.client.getResponse()
        if data is None:
            return
        try:
            header = Cabecalho.from_json(data)
        except Exception as e:
            print("Erro ao processar a resposta do servidor:", str(e))
            return

        print(header.arguments)

    def removerFilme(self):
        print("[Remover]")
        id = int(input("ID: "))
        new_request_id = Cabecalho.increment_request_id()
        cabecalho = Cabecalho(0, "removerFilme", 2, {"id": id}, new_request_id)
        h_json = cabecalho.to_json()
        self.client.sendRequest(h_json)
        data = self.client.getResponse()
        if data is None:
            return
        try:
            header = Cabecalho.from_json(data)
        except Exception as e:
            print("Erro ao processar a resposta do servidor:", str(e))
            return
        
        print(header.arguments)

    def exibirDetalhe(self):
        print("[Exibindo detalhes]")
        id = int(input("ID: "))
        new_request_id = Cabecalho.increment_request_id()
        cabecalho = Cabecalho(0, "exibirDetalhe", 3, {"id": id}, new_request_id)
        h_json = cabecalho.to_json()
        self.client.sendRequest(h_json)
        data = self.client.getResponse()
        if data is None:
            return

        try:
            header = Cabecalho.from_json(data)
            if "Filme nao encontrado!" in header.arguments:
                print("Filme nao encontrado!")
            else:
                filme = Filme.from_json(header.arguments)
                print("------------------")
                print(f"Titulo: {filme.titulo}\nDiretor: {filme.diretor}\nAno: {filme.ano}\nDuração: {filme.duracao}\nGênero: {filme.genero}\nClassificação: {filme.classificacao}\nDescrição: {filme.descricao}")
                print("------------------\n")
        except Exception as e:
            print("Erro ao processar a resposta do servidor:", str(e))
            return

        

    def mostrarCatalogo(self):
        print("[Exibir catálogo]")
        new_request_id = Cabecalho.increment_request_id()
        cabecalho = Cabecalho(0, "mostrarCatalogo", 4, "", new_request_id)
        h_json = cabecalho.to_json()

        self.client.sendRequest(h_json)
        data = self.client.getResponse()
        
        if data is None:
            return
        
        try:
            header = Cabecalho.from_json(data)
        except Exception as e:
            print("Erro ao processar a resposta do servidor:", str(e))
            return
        
        if "Catalogo vazio!" in header.arguments:
            print("Catálogo vazio!")
        else:
            for filme in header.arguments:
                print("------------------")
                print(f"ID: {filme[0]}\nTitulo: {filme[1]}")
                print("------------------\n")