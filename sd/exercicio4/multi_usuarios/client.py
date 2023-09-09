import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except Exception as e:
            print("[ERRO] " + str(e))
            break

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

username = input("Digite seu nome de usuário: ")
client_socket.send(username.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

while True:
    message = input()
    if message.lower() == '/sair':
        client_socket.send('/sair'.encode('utf-8'))
        break
    client_socket.send(message.encode('utf-8'))

client_socket.close()