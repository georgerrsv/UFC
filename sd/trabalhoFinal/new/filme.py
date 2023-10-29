from json import *

class Filme:
    def __init__(self, titulo, diretor, ano, duracao, genero, classificacao, descricao):
        self.id=None
        self.titulo=titulo
        self.diretor=diretor
        self.ano=ano
        self.duracao=duracao
        self.genero=genero
        self.classificacao=classificacao
        self.descricao=descricao
        

    def to_json(self):
        return dumps(self.__dict__)
    
    @classmethod
    def from_json(cls, json_str):
        film_data=loads(json_str)
        return cls(**film_data)