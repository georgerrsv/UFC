import psycopg2
import json

class DBConnection:
    def __init__(self, host, database, user, password, port):
        try:
            self.connection = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password,
                port=port
            )
            self.cursor = self.connection.cursor()
            print("Conexão com o banco de dados estabelecida!")
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def adicionarFilme(self, filme):
        try:
            check_query = "SELECT id FROM filme WHERE titulo = %s AND diretor = %s"
            self.cursor.execute(check_query, (filme.titulo, filme.diretor))
            existing_id = self.cursor.fetchone()
            if existing_id:
                return json.dumps({"error": "Filme já cadastrado!"})

            insert_query = "INSERT INTO filme (titulo, diretor, ano, duracao, genero, classificacao, descricao) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(insert_query, (filme.titulo, filme.diretor, filme.ano, filme.duracao, filme.genero, filme.classificacao, filme.descricao))
            self.connection.commit()
            return json.dumps({"message": "Filme cadastrado com sucesso!"})
        except psycopg2.Error as e:
            self.connection.rollback()
            print("Erro ao adicionar filme:", str(e))
            return json.dumps({"error": "Erro ao adicionar filme!"})
        

    def removerFilme(self, id):
        try:
            check_query = "SELECT id FROM filme WHERE id = %s"
            self.cursor.execute(check_query, (id,))
            existing_id = self.cursor.fetchone()
            if not existing_id:
                return json.dumps({"error": "Filme não encontrado!"})

            delete_query = "DELETE FROM filme WHERE id = %s"
            self.cursor.execute(delete_query, (id,))
            self.connection.commit()
            return json.dumps({"message": "Filme removido com sucesso!"})
        except psycopg2.Error as e:
            self.connection.rollback()
            return json.dumps({"error": "Erro ao remover filme: " + str(e)})
        

    def exibirDetalhe(self, id):
        try:
            check_query = "SELECT id FROM filme WHERE id = %s"
            self.cursor.execute(check_query, (id,))
            existing_id = self.cursor.fetchone()
            print(f"Verificando filme com ID {id}")
            if not existing_id:
                print(f"Filme com ID {id} não encontrado no catálogo.")
                return json.dumps({"error": "Filme nao encontrado no banco de dados"})

            query = "SELECT titulo, diretor, ano, duracao, genero, classificacao, descricao FROM filme WHERE id = %s"
            self.cursor.execute(query, (id,))
            filme_data = self.cursor.fetchone()
            if filme_data:
                print(f"Detalhes do filme com ID {id} encontrados: {filme_data}")

                filme_dict = {
                    "Titulo": filme_data[0],
                    "diretor": filme_data[1],
                    "ano": filme_data[2],
                    "duracao": filme_data[3],
                    "genero": filme_data[4],
                    "classificacao": filme_data[5],
                    "descricao": filme_data[6]
                }
                return json.dumps(filme_dict)
            else:
                print(f"Detalhes do filme com ID {id} não encontrados.")
                return json.dumps({"error": "Detalhes do filme não encontrados"})
        except psycopg2.Error as e:
            return json.dumps({"error": "Erro ao exibir detalhes do filme: " + str(e)})
        

    def mostrarCatalogo(self):
        try:
            query = "SELECT titulo, diretor, ano, duracao, genero, classificacao, descricao FROM filme"
            self.cursor.execute(query)
            filmes_data = self.cursor.fetchall()
            catalogo = []

            for filme_data in filmes_data:
                filme_dict = {
                    "titulo": filme_data[0],
                    "diretor": filme_data[1],
                    "ano": filme_data[2],
                    "duracao": filme_data[3],
                    "genero": filme_data[4],
                    "classificacao": filme_data[5],
                    "descricao": filme_data[6]
                }
                catalogo.append(filme_dict)

            return json.dumps(catalogo)
        except psycopg2.Error as e:
            return json.dumps({"error": "Erro ao exibir catálogo: " + str(e)})