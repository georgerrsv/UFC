from ui import UI
from operation import FilmOperations

server_address = ("localhost", 12345)
film_ops = FilmOperations(server_address)

if __name__ == "__main__":
    ui = UI(film_ops.add_film, film_ops.remove_film, film_ops.list_film, film_ops.list_catalog)
    ui.run()