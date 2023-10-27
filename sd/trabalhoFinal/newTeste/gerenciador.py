from filme import *

class Gerenciador:
    def __init__(self, esqueleto):
        self.esqueleto = esqueleto

    def adicionarFilme(self, titulo, diretor, ano, duracao, genero, classificacao, descricao):
        filme = Filme(titulo=titulo, diretor=diretor, ano=int(ano), duracao=int(duracao), genero=genero, classificacao=int(classificacao), descricao=descricao)
        return self.esqueleto.adicionarFilme(filme)
    
    def removerFilme(self, id):
        return self.esqueleto.removerFilme(id)
    
    def exibirDetalhe(self, id):
        return self.esqueleto.exibirDetalhe(id)
    
    def listarCatalogo(self):
        return self.esqueleto.listarCatalogo()