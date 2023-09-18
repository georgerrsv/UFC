import socket
import time

def singlethread_client():
    host = '127.0.0.1'
    port = 12345
    data = "FIB,35"

    clientes = 20

    for i in range(clientes):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        client_socket.send(data.encode('utf-8'))
        response = client_socket.recv(1024)
        client_socket.close()
        time.sleep(0.1)

start_time = time.time()

singlethread_client()

end_time = time.time()
total_time = end_time - start_time
print(f"Tempo total para o servidor singlethread: {total_time} segundos")
