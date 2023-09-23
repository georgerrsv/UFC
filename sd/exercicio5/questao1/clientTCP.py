import threading
import socket
import time

def multithread_client():
    host = '127.0.0.1'
    port = 12346
    data = "SUM,1,2"
    
    clientes = 100

    for i in range(clientes):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((host, port))
            client_socket.send(data.encode('utf-8'))
            response = client_socket.recv(1024)
        except Exception as e:
            print("Erro no cliente:", str(e))
        finally:
            client_socket.close()

start_time = time.time()
multithread_client()
end_time = time.time()
total_time = end_time - start_time
print(f"Tempo total para o servidor multithread: {total_time} segundos")

def singlethread_client():
    host = '127.0.0.1'
    port = 12345
    data = "SUM,1,2"

    clientes = 100

    for i in range(clientes):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((host, port))
            client_socket.send(data.encode('utf-8'))
            response = client_socket.recv(1024)
        except Exception as e:
            print("Erro no cliente:", str(e))
        finally:
            client_socket.close()

start_time = time.time()
singlethread_client()
end_time = time.time()
total_time = end_time - start_time
print(f"Tempo total para o servidor singlethread: {total_time} segundos")