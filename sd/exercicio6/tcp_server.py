import socket

class TCPServer:
    def __init__(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)

    def aceitarConexao(self):
        return self.server_socket.accept()

    def close(self):
        self.server_socket.close()
