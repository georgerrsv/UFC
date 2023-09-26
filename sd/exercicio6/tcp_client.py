import socket
import pickle

class TCPClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def send_request(self, request):
        self.client_socket.send(pickle.dumps(request))

    def get_response(self):
        response = self.client_socket.recv(1024)
        return pickle.loads(response)

    def close(self):
        self.client_socket.close()
