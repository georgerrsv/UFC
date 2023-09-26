from proxy import Proxy

def handle_client(proxy):

    while True:
        print("Escolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        choice = input("Digite o número da operação desejada: ")

        if choice == '5':
            break

        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if choice == '1':
                result = proxy.invoke('soma', a, b)
            elif choice == '2':
                result = proxy.invoke('sub', a, b)
            elif choice == '3':
                result = proxy.invoke('mult', a, b)
            elif choice == '4':
                result = proxy.invoke('div', a, b)
            else:
                print("Escolha inválida")
                continue

            print(f"Resultado: {result}")
        except ValueError:
            print("Entrada inválida. Certifique-se de que os números estão corretos.")

    proxy.close()