import socket

class UDPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(5)

    def sendRequest(self, request):
        try:
            self.socket.sendto(request.encode('utf-8'), (self.host, self.port))
        except Exception as e:
            return str(e)

    def getResponse(self):
        try:
            data, _ = self.socket.recvfrom(4096)
            return data.decode('utf-8')
        except Exception as e:
            return str(e)

    def close(self):
        self.socket.close()