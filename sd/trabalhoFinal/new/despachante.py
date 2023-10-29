import json
from cabecalho import Cabecalho
from esqueleto import Esqueleto

class Despachante:
    def __init__(self):
        self.esqueleto = Esqueleto()

    def invoke(self, request):
        request_data = json.loads(request)
        cabecalho = Cabecalho(**request_data)

        result = None

        if cabecalho.methodId == 1:
            filme = cabecalho.arguments["filme"]
            result = self.esqueleto.adicionarFilme(filme)
        elif cabecalho.methodId == 2:
            id = cabecalho.arguments["id"]
            result = self.esqueleto.removerFilme(id)
        elif cabecalho.methodId == 3:
            id = cabecalho.arguments["id"]
            result = self.esqueleto.exibirDetalhe(id)
        elif cabecalho.methodId == 4:
            result = self.esqueleto.mostrarCatalogo()

        response_data = {
            "result": result
        }
        response = json.dumps(response_data)
        return response