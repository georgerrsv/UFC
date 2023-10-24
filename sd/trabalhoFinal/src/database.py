import psycopg2
from filme_pb2 import Filme

class DatabaseConnection:
    def __init__(self, host, port, dbname, user, password):
        self.connection = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor()

    def add_film(self, film):
        try:
            self.cursor.execute(
                "INSERT INTO filme (titulo, diretor, ano, duracao, genero, classificacao, descricao)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (film.titulo, film.diretor, film.ano, film.duracao, film.genero, film.classificacao, film.descricao)
            )
            self.connection.commit()
        except Exception as e:
            print(f"Erro ao adicionar filme: {str(e)}")

    def remove_film(self, film_id):
        try:
            self.cursor.execute("DELETE FROM filme WHERE id = %s", (film_id,))
            self.connection.commit()
        except Exception as e:
            print(f"Erro ao remover filme: {str(e)}")

    def list_film(self, film_id):
        try:
            self.cursor.execute("SELECT titulo, diretor, ano, duracao, genero, classificacao, descricao FROM filme WHERE id = %s", (film_id,))
            row = self.cursor.fetchone()
            if row:
                film = Filme()
                film.titulo, film.diretor, film.ano, film.duracao, film.genero, film.classificacao, film.descricao = row
                return film
            else:
                return None
        except Exception as e:
            print(f"Erro ao listar filme: {str(e)}")

    def list_catalog(self):
        try:
            self.cursor.execute("SELECT titulo, diretor, ano, duracao, genero, classificacao, descricao FROM filme")
            rows = self.cursor.fetchall()
            film = Filme()
            catalog = []
            for row in rows:
                film.titulo, film.diretor, film.ano, film.duracao, film.genero, film.classificacao, film.descricao = row
                catalog.append(film)
            return catalog
        except Exception as e:
            print(f"Erro ao listar catálogo: {str(e)}")