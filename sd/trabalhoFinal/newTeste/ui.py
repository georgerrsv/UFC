from proxy import Proxy
from udpClient import UDPClient
import json
import time
import socket

class UserInterface:
    def run(self):
        host = 'localhost'
        port = 12345

        udp_client = UDPClient(host, port)

        while True:
            print("\nEscolha uma operação:")
            print("1. Adicionar Filme")
            print("2. Remover Filme")
            print("3. Exibir Detalhe")
            print("4. Mostrar Catálogo")
            print("5. Sair")

            choice = input("Opção: ")
            try:
                if choice == "1":
                    print()
                    print("[Adicionando Filme]:\n")
                    titulo = input("Título: ")
                    diretor = input("Diretor: ")
                    ano = input("Ano: ")
                    duracao = input("Duração: ")
                    genero = input("Gênero: ")
                    classificacao = input("Classificação: ")
                    descricao = input("Descrição: ")
                    request = f"adicionarFilme {titulo} {diretor} {ano} {duracao} {genero} {classificacao} {descricao}"
                    udp_client.sendRequest(request)
                    response = udp_client.getResponse()
                    try:
                        filme = json.loads(response)
                        if "error" in filme:
                            print(filme["error"])
                        else:
                            print("\nFilme cadastrado com sucesso!")
                    except json.JSONDecodeError:
                        print("Erro: Servidor indisponível!")


                elif choice == "2":
                    print()
                    print("[Remover Filme]\n")
                    id = input("ID: ")
                    request = f"removerFilme {id}"
                    udp_client.sendRequest(request)
                    response = udp_client.getResponse()
                    try:
                        filme = json.loads(response)
                        if "error" in filme:
                            print(filme["error"])
                        else:
                            print("\nFilme removido com sucesso!")
                    except json.JSONDecodeError:
                        print("\nErro: Servidor indisponível!")

                elif choice == "3":
                    print()
                    print("[Exibindo detalhes do filme]\n")
                    id = input("ID do filme a ser exibido: ")
                    print()
                    request = f"exibirDetalhe {id}"
                    udp_client.sendRequest(request)
                    response = udp_client.getResponse()
                    filme = json.loads(response)
                    try:
                        if "error" in filme:
                            print(filme["error"])
                        else:
                            print("Título:", filme["Titulo"])
                            print("Diretor:", filme["diretor"])
                            print("Ano:", filme["ano"])
                            print("Duração:", filme["duracao"])
                            print("Gênero:", filme["genero"])
                            print("Classificação:", filme["classificacao"])
                            print("Descrição:", filme["descricao"])
                    except json.JSONDecodeError:
                        print("\nErro: Servidor indisponível!")        

                elif choice == "4":
                    print()
                    print("[Exibindo catálogo]\n")
                    request = "mostrarCatalogo"
                    udp_client.sendRequest(request)
                    response = udp_client.getResponse()
    
                    try:
                        catalogo = json.loads(response)
                        if "error" in catalogo:
                            print(catalogo["error"])
                        else:
                            for filme in catalogo:
                                print(f"Título: {filme['titulo']}\nDiretor: {filme['diretor']}\nAno: {filme['ano']}\nDuração: {filme['duracao']}\nGênero: {filme['genero']}\nClassificação: {filme['classificacao']}\nDescrição: {filme['descricao']}\n")
                    except json.JSONDecodeError:
                        print("\nErro: Servidor indisponível!")
                elif choice == "5":
                    print("Encerrando programa...")
                    time.sleep(1)
                    udp_client.close()
                    break
                else:
                    print("Opção inválida")
            except socket.timeout:
                    print("Erro: Tempo limite de conexão excedido!")



if __name__ == '__main__':
    user_interface = UserInterface()
    user_interface.run()