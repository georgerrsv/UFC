from udpClient import UDPClient
import json
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
        
        if "Filme nao encontrado!" in data:
            print("\nFilme nao encontrado!\n")
            return

        try:
            header = Cabecalho.from_json(data)
            filme = Filme.from_json(header.arguments)

            print("\n------------------")
            print(f"Titulo: {filme.titulo}\nDiretor: {filme.diretor}\nAno: {filme.ano}\nDuração: {filme.duracao}\nGênero: {filme.genero}\nClassificação: {filme.classificacao}\nDescrição: {filme.descricao}")
            print("------------------\n")

        except Exception as e:
            print("Erro ao processar a resposta do servidor:", str(e))
            return

    def mostrarCatalogo(self):
        data = self.doOperation("filme", 4, "")
        
        if data is None:
            return

        if "Catalogo vazio!" in data:
            print("\nCatalogo vazio!\n")
            return
        
        try:
            header = Cabecalho.from_json(data)
            catalogo = json.loads(header.arguments)
            for filme in catalogo:
                print("\n------------------")
                print(f"ID: {filme['id']}\nTitulo: {filme['titulo']}")
                print("------------------\n")
        except Exception as e:
            print("Erro ao processar a resposta do servidor:", str(e))
            return
            


    def doOperation(self, objectReference, methodId, arguments):
        new_request_id = Cabecalho.increment_request_id()
        cabecalho = Cabecalho(0, objectReference, methodId, arguments, new_request_id)
        h_json = cabecalho.to_json()
        self.client.sendRequest(h_json)
        data = self.client.getResponse()
        return data