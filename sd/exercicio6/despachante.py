# despachante.py

class Despachante:
    def __init__(self, esqueleto):
        self.esqueleto = esqueleto

    def dispatch_request(self, request):
        method_name = request['method']
        args = request['args']
        method = getattr(self.esqueleto, method_name)
        result = method(*args)
        return result