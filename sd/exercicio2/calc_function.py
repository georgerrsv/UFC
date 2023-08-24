def handle_client(client_socket, calculator):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            print('Conexão encerrada pelo cliente')
            break

        try:
            option, valueX, valueY = data.split(',')
            valueX = float(valueX)
            valueY = float(valueY)

            if hasattr(calculator, option):
                method = getattr(calculator, option)
                result = method(valueX, valueY)
            else:
                result = 'Operação inválida'
        except Exception as e:
            result = str(e)

        client_socket.send(str(result).encode('utf-8'))