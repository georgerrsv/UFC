import socket
import threading
from calculator import Calculator

class CalculatorServer:
    def __init__(self):
        self.calculator = Calculator()

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                print('Conexão encerrada pelo cliente')
                break

            try:
                operation, value1, value2 = data.split(',')
                value1 = float(value1)
                value2 = float(value2)

                if operation == 'soma':
                    result = self.calculator.sum(value1, value2)
                elif operation == 'subtracao':
                    result = self.calculator.sub(value1, value2)
                else:
                    result = 'Operação inválida'
            except Exception as e:
                result = str(e)

            client_socket.send(str(result).encode('utf-8'))

        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(10)

    print('Servidor da Calculadora iniciado. Aguardando conexões...')

    calculator_server = CalculatorServer()

    while True:
        client_socket, addr = server.accept()
        print(f'Conexão estabelecida com cliente no IP: {addr[0]} na porta: {addr[1]}')

        client_thread = threading.Thread(target=calculator_server.handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    main()