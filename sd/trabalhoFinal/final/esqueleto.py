from json import *
from database import Database
from filme import Filme

class Esqueleto:
    def __init__(self):
        self.db = Database()
        self.movies = []

    def adicionar_filme(self, request_data):
        try:
            filme_json = request_data.get("arguments")
            filme = Filme.from_json(filme_json)
            result = self.db.adicionarFilme(filme)
            return {"result": result}
        except JSONDecodeError as e:
            return {"result": f"Erro ao desserializar o filme JSON: {str(e)}"}

    def remover_filme(self, request_data):
        id = request_data.get("arguments")
        result = self.db.removerFilme(id)
        return {"result": result}

    def exibir_detalhe(self, request_data):
        id = request_data.get("arguments")
        result = self.db.exibirDetalhe(id)
        return {"result": result}

    def mostrar_catalogo(self):
        result = self.db.mostrarCatalogo()
        return {"result": result}
