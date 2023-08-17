import socket

class Calculator:
    def sum(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mult(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero não é permitida."

def handle_client(client_socket):
    calc = Calculator()
    
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            print("Conexão encerrada pelo cliente.")
            break
        
        try:
            option, value1, value2 = data.split(',')
            value1 = float(value1)
            value2 = float(value2)
            
            if option == 'soma':
                result = calc.sum(value1, value2)
            elif option == 'subtracao':
                result = calc.sub(value1, value2)
            elif option == 'multiplicacao':
                result = calc.mult(value1, value2)
            elif option == 'divisao':
                result = calc.div(value1, value2)
            else:
                result = "Operação inválida"
        except Exception as e:
            result = str(e)
        
        client_socket.send(str(result).encode('utf-8'))

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(5)
    
    print("Servidor TCP aguardando conexões...")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Conexão recebida de {addr}")
        
        handle_client(client_socket)

if __name__ == "__main__":
    main()