from database import Database
from filme import Filme

class Esqueleto:
    def __init__(self):
        self.db = Database()
        self.movies = []

    def adicionarFilme(self, filme_data):
        filme = Filme.from_json(filme_data)
        result = self.db.adicionarFilme(filme)
        if result == "Filme cadastrado com sucesso!":
            self.movies.append(filme)
        return result

    def removerFilme(self, id):
        result = self.db.removerFilme(id)
        if result == "Filme removido com sucesso!":
            for movie in self.movies:
                if movie.id == id:
                    self.movies.remove(movie)
        return result

    def exibirDetalhe(self, id):
        return self.db.exibirDetalhe(id)

    def mostrarCatalogo(self):
        return self.db.mostrarCatalogo()