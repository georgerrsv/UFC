import socket
from dbConnection import DBConnection
from despachante import Despachante

class UDPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        self.db_connection = DBConnection(db_host, db_database, db_user, db_password, db_port)
        self.despachante = Despachante(self.db_connection)
        self.catalogo = self.db_connection.mostrarCatalogo()

    def getRequest(self):
        data, addr = self.server_socket.recvfrom(4096)
        return data.decode('utf-8'), addr

    def getResponse(self, response, addr):
        self.server_socket.sendto(response.encode('utf-8'), addr)

    def run(self):
        print(f"Servidor UDP iniciado...")
        while True:
            request, addr = self.getRequest()
            print(f"Recebido: {request}")
            response = self.despachante.invoke(request)

            if response is not None:
                self.getResponse(response, addr)
            else:
                response = "Filme não encontrado no catálogo."
                self.getResponse(response, addr)

if __name__ == '__main__':
    host = 'localhost'
    port = 12345
    db_host = 'localhost'
    db_database = 'filme'
    db_user = 'admin'
    db_password = 'admin'
    db_port = 5432
    server = UDPServer(host, port)
    server.run()
