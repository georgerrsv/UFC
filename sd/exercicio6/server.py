from tcp_server import TCPServer
from esqueleto import Esqueleto
from despachante import Despachante
from calculator import Calculadora
import pickle

def main():
    host = 'localhost'
    port = 12345
    server = TCPServer(host, port)
    print(f"Servidor TCP iniciado. Aguardando conexões...")

    while True:
        client_socket, client_addr = server.aceitarConexao()
        print(f"Conexão estabelecida com cliente no IP: {client_addr[0]} e porta: {client_addr[1]}")

        calculadora = Calculadora()
        esqueleto = Esqueleto(calculadora)
        despachante = Despachante(esqueleto)

        try:
            while True:
                request = pickle.loads(client_socket.recv(1024))
                if not request:
                    break
                response = despachante.request(request)
                client_socket.send(pickle.dumps(response))
        except Exception as e:
            print("Conexão encerrada pelo cliente. " + str(e))
        finally:
            client_socket.close()

if __name__ == "__main__":
    main()
