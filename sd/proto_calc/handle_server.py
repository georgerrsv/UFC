import threading
import calculator_pb2
from server_conn import ServerConnection

def handle_client(client_socket):
    try:
        while True:
            request_data = client_socket.recv(1024)
            if not request_data:
                print("Conexão encerrada pelo cliente!")
                break

            request = calculator_pb2.CalculationRequest()
            request.ParseFromString(request_data)

            response = calculator_pb2.CalculationResponse()

            if request.choice == "+":
                response.result = str(request.op1 + request.op2)
            elif request.choice == "-":
                if request.op1 < 0 or request.op2 < 0:
                    response.result = str(request.op1 + request.op2)
                else:
                    response.result = str(request.op1 - request.op2)
            elif request.choice == "*":
                response.result = str(request.op1 * request.op2)
            elif request.choice == "/":
                if request.op2 != 0:
                    response.result = str(request.op1 / request.op2)
                else:
                    response.result = "Erro, divisão por zero não é permitida!"

            client_socket.send(response.SerializeToString())
    except Exception as e:
        print(f"Erro ao lidar com o cliente: {e}")
    finally:
        client_socket.close()

def main():
    server_ip = '127.0.0.1'
    server_port = 12345

    connection = ServerConnection(server_ip, server_port)

    print(f"Servidor aguardando conexões...")

    while True:
        client_sock, addr = connection.accept_client()
        print(f"Conexão estabelecida com cliente com IP: {addr[0]}, e PORTA: {addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client_sock,))
        client_handler.start()

if __name__ == "__main__":
    main()
