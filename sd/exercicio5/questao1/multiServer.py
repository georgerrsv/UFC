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
    server_socket.listen(100)
    
    print(f"Servidor multithread aguardando conexões...")
    
    threads = []
    
    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=serverHandler.handle_client, args=(client_socket, calculator))
        threads.append(client_thread)
        client_thread.start()
    
        for thread in threads:
            thread.join()

if __name__ == '__main__':
    main()
