import socket

host = '127.0.0.1'
port = 12345

def main():
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((host, port))
    except ConnectionRefusedError:
        print("O servidor não está disponível.")
        return

    nome = input('Digite seu nome: ')
    client.send(nome.encode('utf-8'))

    print("Digite /sair a qualquer momento para sair do chat.")

    while True:
        msg = input()
        client.send(msg.encode('utf-8'))
        if msg == '/sair':
            break

    client.close()

if __name__ == '__main__':
    main()