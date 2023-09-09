import socket
import threading
import time

usuarios = {}

def handle_client(client_socket, username):
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg.lower() == '/sair':
                print("(log) " + time.strftime('[%d/%m/%Y - %H:%M:%S] ') + username + " saiu do chat.")
                client_socket.close()
                break
            if msg:
                timestamp = time.strftime('%H:%M:%S')
                broadcast("[" + timestamp + "]: " + username + ": " + msg, client_socket)
        except Exception as e:
            print("[ERRO] " + str(e))
            break

    del usuarios[username]
    client_socket.close()

    broadcast(username + " saiu do chat.", client_socket)


def broadcast(message, sender_socket):
    for client_username, client_socket in usuarios.items():
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode('utf-8'))
            except Exception as e:
                print("[ERRO] " + str(e))
                client_socket.close()
                del usuarios[client_username]

HOST = '0.0.0.0'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print("(INFO) Servidor de chat disponível na porta:", PORT)

while True:
    client_socket, addr = server.accept()
    username = client_socket.recv(1024).decode('utf-8')

    if username not in usuarios:
        usuarios[username] = client_socket
        print("(log) " + time.strftime('[%d/%m/%Y - %H:%M:%S] ') + username + " se conectou ao chat. ")
        client_socket.send("Bem-vindo ao chat! Digite /sair a qualquer momento para sair do chat.".encode('utf-8'))
        broadcast(username + " entrou no chat.", client_socket)

        client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
        client_handler.start()
    else:
        client_socket.send("Este nome de usuário já está em uso. Escolha outro.".encode('utf-8'))
        client_socket.close()