import threading
import socket
import time

def multithread_client():
    host = '127.0.0.1'
    port = 12346
    data = "FIB,35"
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        client_socket.send(data.encode('utf-8'))
        response = client_socket.recv(1024)
    except Exception as e:
        print("Erro no cliente:", str(e))
    finally:
        client_socket.close()

num_clients = 20
threads = []

start_time = time.time()

for i in range(num_clients):
    thread = threading.Thread(target=multithread_client)
    threads.append(thread)
    thread.start()
    time.sleep(0.1)

for thread in threads:
    thread.join()

end_time = time.time()
total_time = end_time - start_time
print(f"Tempo total para o servidor multithread: {total_time} segundos")