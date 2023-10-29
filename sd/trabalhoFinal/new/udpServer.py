from socket import *
from database import Database
from despachante import Despachante

class UDPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket(AF_INET, SOCK_DGRAM)
        self.server.bind((self.host, self.port))
        self.db = Database()

    def getRequest(self):
        despachante = Despachante()
        data, addr = self.server.recvfrom(1024)
        data = data.decode('utf-8')
        response = despachante.invoke(data)
        return response, addr

    def sendResponse(self, response, addr):
        self.server.sendto(response.encode('utf-8'), addr)

if __name__ == "__main__":
    server = UDPServer('localhost', 8080)
    print("Servidor UDP iniciado. Aguardando conexões...")
    while True:
        try:
            response, addr = server.getRequest()
            server.sendResponse(response, addr)
        except Exception as e:
            print(f"Erro no servidor: {e}")
