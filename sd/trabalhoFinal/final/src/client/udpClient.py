from socket import *

class UDPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.count = 0
        self.client = socket(AF_INET, SOCK_DGRAM)
        self.client.settimeout(1)

    def sendRequest(self, obj):
        self.client.sendto(obj.encode('utf-8'), (self.host, self.port))
    
    def close(self):
        self.client.close()

    def getResponse(self):
        try:
            data, addr = self.client.recvfrom(1024)
            return data.decode('utf-8')
        except timeout:
            if self.count < 3:
                print("\nTempo de resposta excedido! Tente novamente.\n")
                self.count += 1
            else:
                print("\nServidor indisponível. Tente novamente mais tarde.\n")
                self.close()
                exit(1)