import socket

def main():
    host = '127.0.0.1'
    calc_port = 12346
    conv_port = 12347

    while True:
        print("Opções:")
        print("1. Calculadora")
        print("2. Conversor de decimal para binário")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            server_port = calc_port
            option = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")
            value1 = input("Digite o primeiro valor: ")
            value2 = input("Digite o segundo valor: ")
        elif choice == '2':
            server_port = conv_port
            option = 'conversor'
            value1 = input("Digite o valor a ser convertido para binário: ")
            value2 = 0
        elif choice == '3':
            print("Encerrando conexão com o servidor...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:

            client_socket.connect((host, server_port))

            request = f"{option},{value1},{value2}"
            client_socket.send(request.encode('utf-8'))

            result = client_socket.recv(1024).decode('utf-8')
            print("Resultado:", result)

        except ConnectionError:
            print("Servidor indisponível. Impossível estabelecer conexão.")

        finally:
            client_socket.close()

if __name__ == "__main__":
    main()
