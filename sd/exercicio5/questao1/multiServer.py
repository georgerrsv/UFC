import socket
import threading
import serverHandler
from calculator import Calculator

def main():
    host = '127.0.0.1'
    port = 12346
    
    calculator = Calculator()
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print(f"Servidor calculadora TCP multithread aguardando conexões...")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão estabelecida com IP: {addr[0]} na porta :{addr[1]}")
        client_thread = threading.Thread(target=serverHandler.handle_client, args=(client_socket, calculator))
        client_thread.start()

if __name__ == '__main__':
    main()
