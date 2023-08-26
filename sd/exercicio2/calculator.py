class Calculator:
    def sum(self, x, y):
        return x + y
    
    def sub(self, x, y):
        if x < 0 or y < 0:
            return x + y
        return x - y
    
    def mult(self, x, y):
        return x * y
    
    def div(self, x, y):
        if y == 0:
            raise Exception("Divisão por zero não é permitida")
        return x / y