import calculator_pb2
from client_conn import ClientConnection

def main():
    server_ip = '127.0.0.1'
    server_port = 12345

    connection = ClientConnection(server_ip, server_port)

    while True:
        print("Digite a operação desejada: [soma, subtracao, multiplicacao, divisao, ou sair]")
        choice = input()
        if choice.lower() == "soma":
            choice = "+"
        elif choice.lower() == "subtracao":
            choice = "-"
        elif choice.lower() == "multiplicacao":
            choice = "*"
        elif choice.lower() == "divisao":
            choice = "/"
        elif choice.lower() == "sair":
            break
        else:
            print("Operação inválida!")
            continue
        print("Digite o primeiro valor: ")
        op1 = int(input())
        print("Digite o segundo valor: ")
        op2 = int(input())

        request = calculator_pb2.CalculationRequest()
        request.op1 = op1
        request.op2 = op2
        request.choice = choice

        connection.send_request(request.SerializeToString())
        response_data = connection.receive_response()

        response = calculator_pb2.CalculationResponse()
        response.ParseFromString(response_data)

        print(f"Resultado: {response.result}")

    connection.close()

if __name__ == "__main__":
    main()
