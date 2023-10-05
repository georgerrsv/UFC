import socket

class ClientConnection:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.server_ip, self.server_port))

    def send_request(self, request):
        self.client.send(request)

    def receive_response(self):
        return self.client.recv(1024)

    def close(self):
        self.client.close()