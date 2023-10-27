import tkinter as tk
from udpClient import UDPClient
import json
from tkinter import scrolledtext
import re

class UserInterface:
    def __init__(self, root, udp_client):
        self.root = root
        self.udp_client = udp_client
        root.title("Catálogo de Filmes")

        self.current_frame = None  # Para alternar entre as diferentes operações
        self.create_main_frame()
        self.message_label = None


    def create_back_button(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.create_main_frame()

    def create_main_frame(self):
        if self.current_frame:
            self.current_frame.destroy()  # Destrua o quadro atual

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        self.choice_label = tk.Label(self.current_frame, text="Escolha uma operação:")
        self.choice_label.pack()

        self.add_movie_button = tk.Button(self.current_frame, text="Adicionar Filme", command=self.create_add_movie_frame)
        self.add_movie_button.pack()

        self.remove_movie_button = tk.Button(self.current_frame, text="Remover Filme", command=self.create_remove_movie_frame)
        self.remove_movie_button.pack()

        self.display_details_button = tk.Button(self.current_frame, text="Exibir Detalhes", command=self.create_display_details_frame)
        self.display_details_button.pack()

        self.show_catalog_button = tk.Button(self.current_frame, text="Mostrar Catálogo", command=self.create_show_catalog_frame)
        self.show_catalog_button.pack()

        self.quit_button = tk.Button(self.current_frame, text="Sair", command=self.root.quit)
        self.quit_button.pack()

    def create_add_movie_frame(self):
        if self.current_frame:
            self.current_frame.destroy()  # Destrua o quadro atual
        add_movie_frame = tk.Frame(self.root)
        add_movie_frame.pack()
        self.current_frame = add_movie_frame

        title_label = tk.Label(add_movie_frame, text="Título:")
        title_label.pack()
        self.title_entry = tk.Entry(add_movie_frame)
        self.title_entry.pack()

        director_label = tk.Label(add_movie_frame, text="Diretor:")
        director_label.pack()
        self.director_entry = tk.Entry(add_movie_frame)
        self.director_entry.pack()

        year_label = tk.Label(add_movie_frame, text="Ano:")
        year_label.pack()
        self.year_entry = tk.Entry(add_movie_frame)
        self.year_entry.pack()

        duration_label = tk.Label(add_movie_frame, text="Duração:")
        duration_label.pack()
        self.duration_entry = tk.Entry(add_movie_frame)
        self.duration_entry.pack()

        genre_label = tk.Label(add_movie_frame, text="Gênero:")
        genre_label.pack()
        self.genre_entry = tk.Entry(add_movie_frame)
        self.genre_entry.pack()

        rating_label = tk.Label(add_movie_frame, text="Classificação:")
        rating_label.pack()
        self.rating_entry = tk.Entry(add_movie_frame)
        self.rating_entry.pack()

        description_label = tk.Label(add_movie_frame, text="Descrição:")
        description_label.pack()
        self.description_entry = tk.Entry(add_movie_frame)
        self.description_entry.pack()

        add_button = tk.Button(add_movie_frame, text="Adicionar", command=self.submit_add_movie)
        add_button.pack()
        back_button = tk.Button(add_movie_frame, text="Voltar", command=self.create_back_button)
        back_button.pack()

    def submit_add_movie(self):
        title = self.title_entry.get()
        director = self.director_entry.get()
        year = self.year_entry.get()
        duration = self.duration_entry.get()
        genre = self.genre_entry.get()
        rating = self.rating_entry.get()
        description = self.description_entry.get()

        request = f"adicionarFilme {title} {director} {year} {duration} {genre} {rating} {description}"
        self.udp_client.sendRequest(request)
        response = self.udp_client.getResponse()

        if not title or not director or not year or not duration or not genre or not rating or not description:
            self.show_message("Erro: Preencha todos os campos!", color="red")
            return

        try:
            movie = json.loads(response)
            if "error" in movie:
                self.show_message(movie["error"], color="red")
            else:
                self.show_message("Filme adicionado com sucesso!", color="green")
                self.clear_add_movie_fields()
        except json.JSONDecodeError:
            self.show_message("Erro: Servidor indisponível!", color="red")

    def clear_add_movie_fields(self):
        self.title_entry.delete(0, tk.END)
        self.director_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    def show_message(self, message, color):
        message_label = tk.Label(self.current_frame, text=message, fg=color)
        message_label.pack()

    def create_remove_movie_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        remove_movie_frame = tk.Frame(self.root)
        remove_movie_frame.pack()
        self.current_frame = remove_movie_frame

        id_label = tk.Label(remove_movie_frame, text="ID:")
        id_label.pack()
        self.id_entry = tk.Entry(remove_movie_frame)
        self.id_entry.pack()

        remove_button = tk.Button(remove_movie_frame, text="Remover", command=self.submit_remove_movie)
        remove_button.pack()
        back_button = tk.Button(remove_movie_frame, text="Voltar", command=self.create_back_button)
        back_button.pack()

    def submit_remove_movie(self):
        movie_id = self.id_entry.get()
    
        if not movie_id:
            self.show_message("Erro: ID do filme não fornecido", color="red")
            return

        request = f"removerFilme {movie_id}"
        self.udp_client.sendRequest(request)
        response = self.udp_client.getResponse()

        try:
            movie = json.loads(response)
            if "error" in movie:
                self.show_message(movie["error"], color="red")
            else:
                self.show_message("Filme removido com sucesso!", color="green")
            self.id_entry.delete(0, tk.END)  # Limpar o campo após a remoção
        except json.JSONDecodeError:
            self.show_message("Erro: Servidor indisponível!", color="red")

    def create_display_details_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        display_details_frame = tk.Frame(self.root)
        display_details_frame.pack()
        self.current_frame = display_details_frame

        id_label = tk.Label(display_details_frame, text="ID do Filme:")
        id_label.pack()
        self.id_entry_display = tk.Entry(display_details_frame)
        self.id_entry_display.pack()

        display_button = tk.Button(display_details_frame, text="Exibir", command=self.submit_display_details)
        display_button.pack()
        back_button = tk.Button(display_details_frame, text="Voltar", command=self.create_back_button)
        back_button.pack()

    def submit_display_details(self):
        movie_id = self.id_entry_display.get()
        request = f"exibirDetalhe {movie_id}"
        self.udp_client.sendRequest(request)
        response = self.udp_client.getResponse()

        if not movie_id:
            self.show_message("Erro: Informe um ID!", color="red")
            return

        try:
            movie = json.loads(response)
            if "error" in movie:
                self.show_message(movie["error"], color="red")
            else:
                details = f"Título: {movie['Titulo']}\nDiretor: {movie['diretor']}\nAno: {movie['ano']}\nDuração: {movie['duracao']}\nGênero: {movie['genero']}\nClassificação: {movie['classificacao']}\nDescrição: {movie['descricao']}\n"
                self.show_message(details, color="green")
            self.id_entry_display.delete(0, tk.END)
        except json.JSONDecodeError:
            self.show_message("Erro: Servidor indisponível!", color="red")

    def create_show_catalog_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        show_catalog_frame = tk.Frame(self.root)
        show_catalog_frame.pack()
        self.current_frame = show_catalog_frame
        back_button = tk.Button(show_catalog_frame, text="Voltar", command=self.create_back_button)
        back_button.pack()


        request = "mostrarCatalogo"
        self.udp_client.sendRequest(request)
        response = self.udp_client.getResponse()

        try:
            catalog = json.loads(response)
            if "error" in catalog:
                self.show_message(catalog["error"], color="red")
            else:
                catalog_text = scrolledtext.ScrolledText(show_catalog_frame, wrap=tk.WORD, width=40, height=20)
                catalog_text.pack()
                for movie in catalog:
                    details = f"Título: {movie['titulo']}\nDiretor: {movie['diretor']}\nAno: {movie['ano']}\nDuração: {movie['duracao']}\nGênero: {movie['genero']}\nClassificação: {movie['classificacao']}\nDescrição: {movie['descricao']}\n\n"
                    catalog_text.insert(tk.END, details)
                catalog_text.configure(state='disabled')  # Impede a edição do texto
        except json.JSONDecodeError:
            self.show_message("Erro: Servidor indisponível!", color="red")

    def show_message(self, message, color, timeout=1500):
        if self.message_label:
            self.message_label.destroy()
        self.message_label = tk.Label(self.current_frame, text=message, fg=color)
        self.message_label.pack()

        self.root.after(timeout, self.clear_message)

    def clear_message(self):
        if self.message_label:
            self.message_label.destroy()
            self.message_label = None

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    host = 'localhost'
    port = 12345

    root = tk.Tk()
    udp_client = UDPClient(host, port)
    user_interface = UserInterface(root, udp_client)
    user_interface.run()