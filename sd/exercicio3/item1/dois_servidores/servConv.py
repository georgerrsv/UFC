import socket

def conversor_binario(str_decimal):
    int_decimal = int(str_decimal)
    str_binario = bin(int_decimal)[2:]
    return str_binario

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            print("Conexão encerrada pelo cliente.")
            break
        
        try:
            option, value1, value2 = data.split(',')
            option == 'conversor'
            value_decimal = float(value1)
            value2 = float(value2)
            result = conversor_binario(value_decimal)
        except ValueError:
            result = "Valor inválido."
        
        client_socket.send(result.encode('utf-8'))

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12347))
    server.listen(5)
    
    print("Servidor de conversão aguardando conexões...")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Conexão establecida com cliente com IP: {addr[0]} e porta: {addr[1]}")
        
        handle_client(client_socket)

if __name__ == "__main__":
    main()
