import socket
import serverHandler
from calculator import Calculator

def main():
    host = '127.0.0.1'
    port = 12345
    
    calculator = Calculator()
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print(f"Servidor calculadora TCP aguardando conexões...")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão estabelecida com IP: {addr[0]} e porta :{addr[1]}")
        serverHandler.handle_client(client_socket, calculator)

if __name__ == '__main__':
    main()
