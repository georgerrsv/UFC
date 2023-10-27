from filme import Filme

class Esqueleto:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador

    def adicionarFilme(self, filme_data):
        filme = Filme.from_json(filme_data)
        response = self.gerenciador.adicionarFilme(filme)
        return response

    def removerFilme(self, id):
        response = self.gerenciador.removerFilme(id)
        return response

    def exibirDetalhe(self, id):
        response = self.gerenciador.exibirDetalhe(id)
        return response

    def listarCatalogo(self):
        response = self.gerenciador.listarCatalogo()
        return response