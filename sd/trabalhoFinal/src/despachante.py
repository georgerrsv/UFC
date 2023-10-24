class Despachante:
    def __init__(self, esqueleto):
        self.esqueleto = esqueleto

    def dispatch_request(self, request):
        response = self.esqueleto.process_request(request)
        return response