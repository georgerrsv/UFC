class Calculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Calculator, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        # Inicialize quaisquer recursos necessários aqui
        pass

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
            print("Erro: Divisão por zero")
        return x / y
