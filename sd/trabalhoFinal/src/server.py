import socket
from proxy import Proxy
from esqueleto import Esqueleto
from despachante import Despachante
from database import DatabaseConnection
from filme_pb2 import Request

server_address = ("localhost", 12345)
database = DatabaseConnection('localhost', 5432, 'filme', 'admin', 'admin')
esqueleto = Esqueleto(database)
despachante = Despachante(esqueleto)

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(server_address)

print("Aguardando conexão...")
while True:
    data, client_address = udp_socket.recvfrom(4096)
    request = Request()
    request.ParseFromString(data)
    response = despachante.dispatch_request(request)
    udp_socket.sendto(response.SerializeToString(), client_address)