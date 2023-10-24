import socket
from filme_pb2 import Request

class Proxy:
    def __init__(self, server_address):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = server_address

    def remote_call(self, request):
        try:
            self.udp_socket.sendto(request.SerializeToString(), self.server_address)
            data, _ = self.udp_socket.recvfrom(4096)
            response = Request()
            response.ParseFromString(data)
            return response
        except Exception as e:
            print(f"Erro ao chamar método remoto: {str(e)}")