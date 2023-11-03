import json
from esqueleto import Esqueleto
from filme import Filme

class Despachante:
    def __init__(self):
        self.esqueleto = Esqueleto()

    def invoke(self, request):
        request_data = json.loads(request)
        methodId = request_data.get("methodId")

        if methodId == 1:
            response = self.esqueleto.adicionar_filme(request_data)
        elif methodId == 2:
            response = self.esqueleto.remover_filme(request_data)
        elif methodId == 3:
            response = self.esqueleto.exibir_detalhe(request_data)
        elif methodId == 4:
            response = self.esqueleto.mostrar_catalogo()

        response_data = {
            "messageType": 0,
            "objectreference": request_data.get("objectreference"),
            "methodId": methodId,
            "arguments": response.get("result"),
            }
        response = json.dumps(response_data)

        return response
