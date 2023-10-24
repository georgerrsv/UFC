from filme_pb2 import Request, AddFilmRequest, RemoveFilmRequest, ListFilmRequest, ListCatalogRequest
from proxy import Proxy

class FilmOperations:
    def __init__(self, server_address):
        self.proxy = Proxy(server_address)

    def add_film(self, titulo, diretor, ano, duracao, genero, classificacao, descricao):
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
        response = self.proxy.remote_call(request)

    def remove_film(self, film_id):
        remove_request = RemoveFilmRequest(id=film_id)
        request = Request(remove_film_request=remove_request)
        response = self.proxy.remote_call(request)

    def list_film(self, film_id):
        list_request = ListFilmRequest(id=film_id)
        request = Request(list_film_request=list_request)
        response = self.proxy.remote_call(request)

    def list_catalog(self):
        request = Request(list_catalog_request=ListCatalogRequest())
        response = self.proxy.remote_call(request)