import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    while True:
        print("Escolha a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Sair")

        choice = input("Digite o número da operação desejada: ")

        if choice == '1':
            operation = 'soma'
        elif choice == '2':
            operation = 'subtracao'
        elif choice == '3':
            break
        else:
            print("Operação inválida")
            continue

        value1 = float(input("Digite o primeiro valor: "))
        value2 = float(input("Digite o segundo valor: "))

        message = f"{operation},{value1},{value2}"
        client_socket.send(message.encode('utf-8'))

        result = client_socket.recv(1024).decode('utf-8')
        print(f"Resultado da operação '{operation}': {result}")

    client_socket.close()

if __name__ == "__main__":
    main()