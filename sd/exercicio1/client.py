import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect(('127.0.0.1', 12345))
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor. Verifique se o servidor está em execução.")
        return
    
    while True:
        operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao; ou 'sair' para sair): ")
        if operacao == 'sair':
            break
        
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        
        mensagem = f"{operacao},{valor1},{valor2}"
        client.send(mensagem.encode('utf-8'))
        
        resultado = client.recv(1024).decode('utf-8')
        print("Resultado:", resultado)

    client.close()

if __name__ == "__main__":
    main()