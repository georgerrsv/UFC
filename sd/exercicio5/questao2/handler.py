from calculator import Calculator

def handle_client(client_socket):
    calculator = Calculator()
    
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            print('Conexão encerrada pelo cliente')
            break

        try:
            option, valor1, valor2 = data.split(',')
            valor1 = float(valor1)
            valor2 = float(valor2)

            if hasattr(calculator, option):
                method = getattr(calculator, option)
                result = method(valor1, valor2)
            else:
                result = 'Operação inválida'
        except Exception as e:
            result = str(e)

        client_socket.send(str(result).encode('utf-8'))
