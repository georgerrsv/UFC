import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect(('127.0.0.1', 12345))
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor. Verifique se o servidor está em execução.")
        return
    
    while True:
        option = input("Digite a operação (soma, subtracao, multiplicacao, divisao; ou sair para encerrar): ")
        if option == 'sair':
            break
        
        value1 = float(input("Digite o primeiro valor: "))
        value2 = float(input("Digite o segundo valor: "))
        
        msg = f"{option},{value1},{value2}"
        client.send(msg.encode('utf-8'))
        
        result = client.recv(1024).decode('utf-8')
        print("Resultado:", result)

    client.close()

if __name__ == "__main__":
    main()