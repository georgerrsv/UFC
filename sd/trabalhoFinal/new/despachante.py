import json
from cabecalho import Cabecalho
from esqueleto import Esqueleto

class Despachante:
    def __init__(self):
        self

    def invoke(self, request):
        esqueleto = Esqueleto()
        request_data = json.loads(request)
        cabecalho = Cabecalho(**request_data)

        result = None

        if cabecalho.methodId == 1:
            filme = cabecalho.arguments["filme"]
            result = esqueleto.adicionarFilme(filme)
        elif cabecalho.methodId == 2:
            id = cabecalho.arguments["id"]
            result = esqueleto.removerFilme(id)
        elif cabecalho.methodId == 3:
            id = cabecalho.arguments["id"]
            result = esqueleto.exibirDetalhe(id)
        elif cabecalho.methodId == 4:
            result = esqueleto.mostrarCatalogo()

        response_data = {
            "messageType": 1,
            "objectreference": "filme",
            "methodId": cabecalho.methodId,
            "arguments": result
        }
        
        response = json.dumps(response_data)
        return response