import socket
import datetime

host = '127.0.0.1'
port = 12345

usuarios = {}

def handle_client(client_socket):
    nome = client_socket.recv(1024).decode('utf-8')
    print(f'{nome} se conectou.')

    while True:
        msg = client_socket.recv(1024).decode('utf-8')
        if msg.lower() == '/sair':
            print(f'{nome} saiu.')
            client_socket.close()
            break
        else:
            hora_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f'{hora_atual} - {nome}: {msg}')

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f'Servidor de chat aguardando conexões...')

    while True:
        client_socket, addr = server.accept()

        client_socket.send('Digite seu nome: '.encode('utf-8'))
        print(f'Conexão com usuário estabelecida no IP {addr[0]} e porta {addr[1]}.')

        usuarios[client_socket] = True

        handle_client(client_socket)

        del usuarios[client_socket]

if __name__ == '__main__':
    main()