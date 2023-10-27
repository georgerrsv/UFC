import json

class Filme:
    def __init__(self, titulo, diretor, ano, duracao, genero, classificacao, descricao):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
        self.duracao = duracao
        self.genero = genero
        self.classificacao = classificacao
        self.descricao = descricao

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(**data)
