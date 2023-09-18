def handle_client(client_socket, calculator):
    try:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            return
        
        command, *args = data.split(',')
        
        if command == 'SUM':
            result = calculator.sum(float(args[0]), float(args[1]))
        elif command == 'FIB':
            result = calculator.fib(int(args[0]))
        else:
            result = "Comando desconhecido"
        
        client_socket.send(str(result).encode('utf-8'))
    except Exception as e:
        print("Erro durante o processamento do cliente:", str(e))
    finally:
        client_socket.close()
