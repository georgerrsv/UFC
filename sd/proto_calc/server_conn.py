import socket

class ServerConnection:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.server_ip, self.server_port))
        self.server.listen(5)

    def accept_client(self):
        return self.server.accept()

    def close(self):
        self.server.close()