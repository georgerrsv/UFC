import socket
import time

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        client_socket.connect((host, port))

        while True:
            print("Opções:")
            print("1. Calculadora")
            print("2. Conversor de decimal para binário")
            print("3. Sair")

            choice = input("Escolha uma opção: ")

            if choice == '1':
                opt = input("Digite a operação: soma (+), subtracao (-), multiplicacao (*), divisao (/): ")
                value1 = input("Digite o primeiro valor: ")
                value2 = input("Digite o segundo valor: ")
            elif choice == '2':
                opt = 'conversor'
                value1 = input("Digite o valor decimal: ")
                value2 = 0
            elif choice == '3':
                print("Encerrando conexão com o servidor...")
                time.sleep(1)
                break
            else:
                print("Opção inválida. Tente novamente.")
                continue

            if choice == '1':
                request = f"{opt},{value1},{value2}"
                client_socket.send(request.encode('utf-8'))
            else:
                request = f"{opt},{value1},{value2}"
                client_socket.send(request.encode('utf-8'))

            result = client_socket.recv(1024).decode('utf-8')
            print("Resultado:", result)

    except ConnectionError:
        print("Não foi possível estabelecer conexão com o servidor! Serviço indisponível.")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()