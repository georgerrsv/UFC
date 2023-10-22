import socket
import psycopg2
from filme_pb2 import *

conn = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    dbname = 'filme',
    user = 'admin',
    password = 'admin'
)

cur = conn.cursor()

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("localhost", 12345)

udp_socket.bind(server_address)

def adicionar_filme(request):
    add_request = request.add_film_request
    filme = Filme()
    filme.titulo = add_request.titulo
    filme.diretor = add_request.diretor
    filme.genero = add_request.genero
    filme.ano = int(add_request.ano)
    filme.duracao = int(add_request.duracao)
    filme.classificacao = int(add_request.classificacao)
    filme.descricao = add_request.descricao

    cur.execute(
        "INSERT INTO filme (titulo, diretor, ano, duracao, genero, classificacao, descricao)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (filme.titulo, filme.diretor, filme.ano, filme.duracao, filme.genero, filme.classificacao, filme.descricao)
    )
    conn.commit()


def remover_filme(request):
    remove_request = request.remove_film_request
    id_filme = remove_request.id
    cur.execute("DELETE FROM filme WHERE id = %s", (id_filme,))
    conn.commit()


def listar_filme(request, client_address):
    list_request = request.list_film_request
    id_filme = list_request.id
    cur.execute("SELECT titulo, diretor, ano, duracao, genero, classificacao, descricao FROM filme WHERE id = %s", (id_filme,))
    filme_data = cur.fetchone()
    response = Response()
    if filme_data is None:
        response.error_message = "Filme não encontrado"
    else:
        titulo, diretor, ano, duracao, genero, classificacao, descricao = filme_data
        filme = Filme(titulo=titulo, diretor=diretor, ano=ano, duracao=duracao, genero=genero, classificacao=classificacao, descricao=descricao)
        response.filme.CopyFrom(filme)
    
    udp_socket.sendto(response.SerializeToString(), client_address)


def listar_catalogo(request):
    try:
        cur.execute("SELECT titulo, diretor, ano, duracao, genero, classificacao, descricao FROM filme")
        filmes_data = cur.fetchall()
        filmes = []
        for filme_data in filmes_data:
            titulo, diretor, genero, ano, duracao, classificacao, descricao = filme_data
            filme = Filme(titulo=titulo, diretor=diretor, genero=genero, ano=ano, duracao=duracao, classificacao=classificacao, descricao=descricao)
            filmes.append(filme)
        response = Response(catalogo=filmes)
    except Exception as e:
        response = Response(error_message="Erro ao listar o catálogo de filmes: " + str(e))
    return response


print("Aguardando conexão...")
while True:
    data, client_address = udp_socket.recvfrom(4096)

    request = Request()
    request.ParseFromString(data)
    response = Response()

    if request.HasField("add_film_request"):
        adicionar_filme(request)
    elif request.HasField("remove_film_request"):
        remover_filme(request)
    elif request.HasField("list_film_request"):
        listar_filme(request, client_address)
    elif request.HasField("list_catalog_request"):
        response = listar_catalogo(request)
    else:
        response.error_message = "Comando inválido"

    print(f"Recebida solicitação: {request}")
    
    udp_socket.sendto(response.SerializeToString(), client_address)
