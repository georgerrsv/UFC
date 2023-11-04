import psycopg2
from filme import Filme

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="filme",
            user="postgres",
            password="admin"
        )
        self.cursor = self.connection.cursor()

    def adicionarFilme(self, filme):
        self.cursor.execute("INSERT INTO filme (titulo, diretor, ano, duracao, genero, classificacao, descricao) VALUES (%s, %s, %s, %s, %s, %s, %s)", (filme.titulo, filme.diretor, filme.ano, filme.duracao, filme.genero, filme.classificacao, filme.descricao))
        self.connection.commit()
        if self.cursor.rowcount == 1:
            return "Filme cadastrado com sucesso!"
        else:
            return "Erro ao cadastrar filme!"
        
    def removerFilme(self, id):
        self.cursor.execute("DELETE FROM filme WHERE id = %s", (id,))
        self.connection.commit()
        if self.cursor.rowcount == 1:
            return "Filme removido com sucesso!"
        else:
            return "Erro ao remover filme!"
        
    def exibirDetalhe(self, id):
        self.cursor.execute("SELECT * FROM filme WHERE id = %s", (id,))
        filme = self.cursor.fetchone()
        if filme:
            return Filme(filme[1], filme[2], filme[3], filme[4], filme[5], filme[6], filme[7]).to_json()
        else:
            return "Filme nao encontrado!"
        
    def mostrarCatalogo(self):
        self.cursor.execute("SELECT id, titulo FROM filme")
        filmes = self.cursor.fetchall()
        if filmes:
            return filmes
        else:
            return "Catalogo vazio!"