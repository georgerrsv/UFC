from connection import clientConnection
from calculator import Calculator

def main():
    connection = clientConnection('127.0.0.1', 12345)
    calculator = Calculator()
    
    while True:
        operacao = input("Digite a operação: sum (+), sub (-), mult (*), div (/); ou 'sair' para sair): ")
        if operacao == 'sair':
            break
        
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        
        mensagem = f"{operacao},{valor1},{valor2}"
        resultado = connection.send_message(mensagem)
        
        print("Resultado:", resultado)

    connection.close()

if __name__ == "__main__":
    main()
