from json import *

class Cabecalho:
    _requestId = 0

    def __init__(self, messageType, requestId, objectreference, methodId, arguments):
        self.messageType = messageType
        self.requestId = Cabecalho._requestId
        self.objectreference = objectreference
        self.methodId = methodId
        self.arguments = arguments
        Cabecalho._requestId += 1

    def to_json(self):
        return dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        try:
            cabecalho_data = loads(json_str)
            # Certifique-se de que o dicionário cabecalho_data contenha os campos esperados
            # cabecalho_data deve ser um dicionário Python que pode ser acessado como um objeto
            # Exemplo de validação:
            if 'messageType' not in cabecalho_data:
                raise ValueError
            if 'requestId' not in cabecalho_data:
                raise ValueError
            if 'objectreference' not in cabecalho_data:
                raise ValueError
            if 'methodId' not in cabecalho_data:
                raise ValueError
            if 'arguments' not in cabecalho_data:
                raise ValueError
            return cls(**cabecalho_data)
        except ValueError:
            raise ValueError("Erro ao converter JSON para cabeçalho")
