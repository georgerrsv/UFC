import json
from database import Database
from filme import Filme

class Esqueleto:
    def __init__(self):
        self.db = Database()

    def adicionar_filme(self, arguments_json):
        arguments = json.loads(arguments_json)
        filme = Filme(**arguments)
        return self.db.adicionarFilme(filme)

    def remover_filme(self, arguments_json):
        arguments = json.loads(arguments_json)
        return self.db.removerFilme(arguments)

    def exibir_detalhe(self, arguments_json):
        arguments = json.loads(arguments_json)
        return self.db.exibirDetalhe(arguments)

    def mostrar_catalogo(self):
        return self.db.mostrarCatalogo()