class Calculator:
    def sum(self, a, b):
        return a + b
    
    def fib(self, a):
        if a <= 0:
            return 0
        elif a == 1:
            return 1
        return self.fib(a - 1) + self.fib(a - 2)