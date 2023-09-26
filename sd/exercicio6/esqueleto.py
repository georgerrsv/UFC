class Esqueleto:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def soma(self, a, b):
        return self.calculadora.soma(a, b)

    def sub(self, a, b):
        return self.calculadora.sub(a, b)

    def mult(self, a, b):
        return self.calculadora.mult(a, b)

    def div(self, a, b):
        return self.calculadora.div(a, b)
