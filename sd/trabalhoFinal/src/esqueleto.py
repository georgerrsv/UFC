from filme_pb2 import Request, Response, Filme

class Esqueleto:
    def __init__(self, database):
        self.database = database

    def process_request(self, request):
        response = Response()

        if request.HasField("add_film_request"):
            film_data = request.add_film_request
            film = Filme(
                id="",
                titulo=film_data.titulo,
                diretor=film_data.diretor,
                ano=film_data.ano,
                duracao=film_data.duracao,
                genero=film_data.genero,
                classificacao=film_data.classificacao,
                descricao=film_data.descricao
            )
            self.database.add_film(film)
            response.filme.CopyFrom(film)
        elif request.HasField("remove_film_request"):
            film_id = request.remove_film_request.id
            self.database.remove_film(film_id)
        elif request.HasField("list_film_request"):
            film_id = request.list_film_request.id
            film = self.database.list_film(film_id)
            if film:
                response.filme.CopyFrom(film)
        elif request.HasField("list_catalog_request"):
            catalog = self.database.list_catalog()
            response.catalogo.extend(catalog)
        else:
            response.error_message = "Comando inválido"
        
        return response