import tkinter as tk
from filme_pb2 import *
import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def enviar_requisicao(requisicao):
    server_address = ("localhost", 12345)
    udp_socket.sendto(requisicao.SerializeToString(), server_address)


def adicionar_filme():
    titulo = titulo_entry.get()
    diretor = diretor_entry.get()
    ano = ano_entry.get()
    duracao = duracao_entry.get()
    genero = genero_entry.get()
    classificacao = classificacao_entry.get()
    descricao = descricao_entry.get()

    add_request = AddFilmRequest(
        titulo=titulo,
        diretor=diretor,
        ano=int(ano),
        duracao=int(duracao),
        genero=genero,
        classificacao=int(classificacao),
        descricao=descricao
    )
    request = Request(add_film_request=add_request)
    enviar_requisicao(request)
    
    titulo_entry.delete(0, tk.END)
    diretor_entry.delete(0, tk.END)
    ano_entry.delete(0, tk.END)
    duracao_entry.delete(0, tk.END)
    genero_entry.delete(0, tk.END)
    classificacao_entry.delete(0, tk.END)
    descricao_entry.delete(0, tk.END)
    
    resultado_label.config(text="Filme cadastrado com sucesso!")

def remover_filme():
    id_filme = id_filme_entry.get()
    remove_request = RemoveFilmRequest(id=id_filme)
    request = Request(remove_film_request=remove_request)
    enviar_requisicao(request)
    
    id_filme_entry.delete(0, tk.END)
    
    resultado_label.config(text="Filme removido com sucesso!")

def listar_filme():
    id_filme = id_filme_entry.get()
    list_request = ListFilmRequest(id=id_filme)
    request = Request(list_film_request=list_request)
    enviar_requisicao(request)
    
    id_filme_entry.delete(0, tk.END)
    
    data, _ = udp_socket.recvfrom(4096)
    response = Response()
    response.ParseFromString(data)
    
    if response.HasField("filme"):
        filme = response.filme
        resultado_label.config(text="Exibindo resultado:\n"
                                 f"Título: {filme.titulo}\n"
                                 f"Diretor: {filme.diretor}\n"
                                 f"Gênero: {filme.genero}\n"
                                 f"Ano: {filme.ano}\n"
                                 f"Duração: {filme.duracao}\n"
                                 f"Classificação: {filme.classificacao}\n"
                                 f"Descrição: {filme.descricao}")
    
    id_filme_entry.delete(0, tk.END)

def listar_catalogo():
    list_catalog = ListCatalogRequest()
    request = Request(list_catalog_request=list_catalog)
    enviar_requisicao(request)
    
    data, _ = udp_socket.recvfrom(4096)
    print(data)
    response = Response()
    response.ParseFromString(data)
    
    if response.HasField("error_message"):
        resultado_label.config(text=response.error_message)
    elif response.HasField("catalogo"):
        filmes = response.catalogo
        resultado = "Exibindo catálogo:\n"
        for filme in filmes:
            resultado += f"Título: {filme.titulo}\n" \
                        f"Diretor: {filme.diretor}\n" \
                        f"Gênero: {filme.genero}\n" \
                        f"Ano: {filme.ano}\n" \
                        f"Duração: {filme.duracao}\n" \
                        f"Classificação: {filme.classificacao}\n" \
                        f"Descrição: {filme.descricao}\n"
        resultado_label.config(text=resultado)
    id_filme_entry.delete(0, tk.END)

def criar_adicionar_filme_widgets():
    titulo_label.pack()
    titulo_entry.pack()
    diretor_label.pack()
    diretor_entry.pack()
    ano_label.pack()
    ano_entry.pack()
    duracao_label.pack()
    duracao_entry.pack()
    genero_label.pack()
    genero_entry.pack()
    classificacao_label.pack()
    classificacao_entry.pack()
    descricao_label.pack()
    descricao_entry.pack()
    adicionar_filme_button.pack()

def criar_remover_filme_widgets():
    id_filme_label.pack()
    id_filme_entry.pack()
    remover_filme_button.pack()

def criar_listar_filme_widgets():
    id_filme_label.pack()
    id_filme_entry.pack()
    listar_filme_button.pack()

def criar_listar_catalogo_widgets():
    listar_catalogo_button.pack()

def ocultar_widgets():
    for widget in widgets:
        widget.pack_forget()

def atualizar_widgets():
    escolha = escolha_var.get()
    ocultar_widgets()

    if escolha == "Adicionar Filme":
        criar_adicionar_filme_widgets()
    elif escolha == "Remover Filme":
        criar_remover_filme_widgets()
    elif escolha == "Listar Filme":
        criar_listar_filme_widgets()
    elif escolha == "Listar Catálogo":
        criar_listar_catalogo_widgets()
    resultado_label.config(text="")

root = tk.Tk()
root.title("Cliente de Filmes")
root.geometry("400x400")

escolha_var = tk.StringVar()
escolha_var.set("Selecione uma opção")

escolha_dropdown = tk.OptionMenu(root, escolha_var, "Selecione uma opção", "Adicionar Filme", "Remover Filme", "Listar Filme", "Listar Catálogo")
escolha_dropdown.pack()

confirmar_escolha_button = tk.Button(root, text="Confirmar Escolha", command=atualizar_widgets)
confirmar_escolha_button.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

titulo_label = tk.Label(root, text="Título:")
titulo_entry = tk.Entry(root)
diretor_label = tk.Label(root, text="Diretor:")
diretor_entry = tk.Entry(root)
ano_label = tk.Label(root, text="Ano:")
ano_entry = tk.Entry(root)
duracao_label = tk.Label(root, text="Duração:")
duracao_entry = tk.Entry(root)
genero_label = tk.Label(root, text="Gênero:")
genero_entry = tk.Entry(root)
classificacao_label = tk.Label(root, text="Classificação:")
classificacao_entry = tk.Entry(root)
descricao_label = tk.Label(root, text="Descrição:")
descricao_entry = tk.Entry(root)
adicionar_filme_button = tk.Button(root, text="Adicionar Filme", command=adicionar_filme)

id_filme_label = tk.Label(root, text="ID do Filme:")
id_filme_entry = tk.Entry(root)
remover_filme_button = tk.Button(root, text="Remover Filme", command=remover_filme)

id_filme_label = tk.Label(root, text="ID do Filme:")
id_filme_entry = tk.Entry(root)
listar_filme_button = tk.Button(root, text="Listar Filme", command=listar_filme)

listar_catalogo_button = tk.Button(root, text="Listar Catálogo", command=listar_catalogo)

widgets = [titulo_label, titulo_entry, diretor_label, diretor_entry, ano_label, ano_entry, duracao_label,
           duracao_entry, genero_label, genero_entry, classificacao_label, classificacao_entry, descricao_label,
           descricao_entry, adicionar_filme_button, id_filme_label, id_filme_entry, remover_filme_button,
           listar_filme_button, listar_catalogo_button]

ocultar_widgets()

root.mainloop()
