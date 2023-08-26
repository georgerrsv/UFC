import socket
import threading
from calculator import Calculator
from calc_function import handle_client

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(10)

    print('Servidor TCP iniciado. Aguardando conexões...')

    calculator = Calculator()

    while True:
        client_socket, addr = server.accept()
        print(f'Conexão estabelecida com cliente no IP {addr[0]} na porta {addr[1]}')

        client_thread = threading.Thread(target=handle_client, args=(client_socket, calculator))
        client_thread.start()


if __name__ == '__main__':
    main()