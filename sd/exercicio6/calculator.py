class Calculadora:
    def soma(self, a, b):
        return a + b

    def sub(self, a, b):
        if a < 0 or b < 0:
            return a + b
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Divisão por zero não é permitida!"
        return a / b