import socket

class Calculator:
    def sum(self, a, b):
        return a + b
    
    def sub(self, a, b):
        if a < 0 or b < 0:
            return a + b
        return a - b
    
    def mult(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b != 0:
            return a / b
        return "Divisão por zero não é permitida."

def handle_calculator_client(client_socket):
    calc = Calculator()
    
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            print("Conexão encerrada pelo cliente.")
            break
        
        try:
            option, num1, num2 = data.split(',')
            num1 = float(num1)
            num2 = float(num2)
            
            if option == 'soma':
                result = calc.sum(num1, num2)
            elif option == 'subtracao':
                result = calc.sub(num1, num2)
            elif option == 'multiplicacao':
                result = calc.mult(num1, num2)
            elif option == 'divisao':
                result = calc.div(num1, num2)
            else:
                result = "Operação inválida"
        except Exception as e:
            result = str(e)
        
        client_socket.send(str(result).encode('utf-8'))

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12346))
    server.listen(5)
    
    print("Servidor da calculadora aguardando conexões...")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Conexão estabelecida com cliente com IP: {addr[0]} e porta: {addr[1]}")
        
        handle_calculator_client(client_socket)

if __name__ == "__main__":
    main()
