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
        self.despachante = Despachante()

    def getRequest(self):
        data, addr = self.server.recvfrom(1024)
        data = data.decode('utf-8')
        return data, addr

    def sendResponse(self, response, addr):
        self.server.sendto(response.encode('utf-8'), addr)

    def run(self):
        print('Servidor UDP iniciado...')
        while True:
            data, addr = self.getRequest()
            print('Recebido de', addr, ':', data)
            response = self.processRequest(data)
            self.sendResponse(response, addr)
            print('Enviado para', addr, ':', response)
            

    def processRequest(self, request):
        response = self.despachante.invoke(request)
        return response

if __name__ == '__main__':
    server = UDPServer('localhost', 8080)
    server.run()