import socket

class clientConnection:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(('127.0.0.1', 12345))
        except ConnectionRefusedError:
            print("Não foi possível estabelecer conexão. Servidor indisponível.")
            raise
    
    def send_message(self, message):
        self.client_socket.send(message.encode('utf-8'))
        return self.client_socket.recv(1024).decode('utf-8')
    
    def close(self):
        self.client_socket.close()