from socket import *
from database import *
from despachante import Despachante

class UDPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket(AF_INET, SOCK_DGRAM)
        self.server.bind((self.host, self.port))
        self.db = Database()

    def getRequest(self):
        despachante=Despachante()
        data, addr = self.server.recvfrom(1024)
        data = data.decode('utf-8')
        response = despachante.invoke(data)
        return response, addr

    def sendResponse(self, response, addr):
        self.server.sendto(response.encode('utf-8'), addr)

server = UDPServer('localhost', 8080)
print("Servidor UDP iniciado. Aguardando conexões...")
while 1:
    response, addr = server.getRequest()
    server.sendResponse(response, addr)