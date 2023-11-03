import json
from esqueleto import Esqueleto

class Despachante:
    def __init__(self):
        self.esqueleto = Esqueleto()

    def invoke(self, request):
        request_data = json.loads(request)
        arguments_json = request_data.get("arguments")
        method_id = request_data.get("methodId")

        if method_id == 1:
            response = self.esqueleto.adicionar_filme(arguments_json)
        elif method_id == 2:
            response = self.esqueleto.remover_filme(arguments_json)
        elif method_id == 3:
            response = self.esqueleto.exibir_detalhe(arguments_json)
        elif method_id == 4:
            response = self.esqueleto.mostrar_catalogo()

        response_data = {
            "messageType": 0,
            "objectreference": request_data.get("objectreference"),
            "methodId": method_id,
            "arguments": response
        }
        return json.dumps(response_data)