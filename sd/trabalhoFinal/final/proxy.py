from udpClient import UDPClient
from json import *
from filme import Filme
from cabecalho import Cabecalho

class Proxy:
    def __init__(self):
        self.client = UDPClient('localhost', 8080)

    def adicionarFilme(self, filme):

        filme_json = filme.to_json()
        data = self.doOperation("filme", 1, filme_json)
        if data is None:
            return
        try:
            header = Cabecalho.from_json(data)
        except Exception as e:
            print("Erro ao processar a resposta do servidor:", str(e))
            return

        print(header.arguments)

    def removerFilme(self, id):
        
        data = self.doOperation("filme", 2, id)
        if data is None:
            return
        try:
            header = Cabecalho.from_json(data)
        except Exception as e:
            print("Erro ao processar a resposta do servidor:", str(e))
            return
        
        print(header.arguments)

    def exibirDetalhe(self, id):
        data = self.doOperation("filme", 3, id)
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
        data = self.doOperation("filme", 4, "")
        
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

    def doOperation(self, objectReference, methodId, arguments):
        new_request_id = Cabecalho.increment_request_id()
        cabecalho = Cabecalho(0, objectReference, methodId, arguments, new_request_id)
        h_json = cabecalho.to_json()
        self.client.sendRequest(h_json)
        data = self.client.getResponse()
        return data