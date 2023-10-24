import tkinter as tk
from tkinter import messagebox

class UI:
    def __init__(self, add_film_func, remove_film_func, list_film_func, list_catalog_func):
        self.root = tk.Tk()
        self.root.title("Cliente de Filmes")
        self.add_film_func = add_film_func
        self.remove_film_func = remove_film_func
        self.list_film_func = list_film_func
        self.list_catalog_func = list_catalog_func

        self.create_ui()

    def create_ui(self):
        self.choice_var = tk.StringVar()
        self.choice_var.set("Selecione uma opção")

        self.choice_dropdown = tk.OptionMenu(self.root, self.choice_var, "Selecione uma opção", "Adicionar Filme", "Remover Filme", "Listar Filme", "Exibir Catálogo", "Sair")
        self.choice_dropdown.pack()

        self.confirm_choice_button = tk.Button(self.root, text="Confirmar Escolha", command=self.handle_choice)
        self.confirm_choice_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def handle_choice(self):
        choice = self.choice_var.get()
        if choice == "Adicionar Filme":
            self.create_add_film_widgets()
        elif choice == "Remover Filme":
            self.create_remove_film_widgets()
        elif choice == "Listar Filme":
            self.create_list_film_widgets()
        elif choice == "Exibir Catálogo":
            self.create_list_catalog_widgets()
        elif choice == "Sair":
            self.root.quit()
        else:
            messagebox.showerror("Erro", "Escolha inválida")


    def create_add_film_widgets(self):
        self.clear_widgets()

        titulo_label = tk.Label(self.root, text="Título:")
        titulo_entry = tk.Entry(self.root)
        diretor_label = tk.Label(self.root, text="Diretor:")
        diretor_entry = tk.Entry(self.root)
        ano_label = tk.Label(self.root, text="Ano:")
        ano_entry = tk.Entry(self.root)
        duracao_label = tk.Label(self.root, text="Duração:")
        duracao_entry = tk.Entry(self.root)
        genero_label = tk.Label(self.root, text="Gênero:")
        genero_entry = tk.Entry(self.root)
        classificacao_label = tk.Label(self.root, text="Classificação:")
        classificacao_entry = tk.Entry(self.root)
        descricao_label = tk.Label(self.root, text="Descrição:")
        descricao_entry = tk.Entry(self.root)
        adicionar_filme_button = tk.Button(self.root, text="Adicionar Filme", command=lambda: self.handle_add_film(
            titulo_entry.get(), diretor_entry.get(), ano_entry.get(), duracao_entry.get(), genero_entry.get(),
            classificacao_entry.get(), descricao_entry.get()
        ))

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

        voltar_button = tk.Button(self.root, text="Voltar", command=self.create_ui)
        voltar_button.pack()

    def create_remove_film_widgets(self):
        self.clear_widgets()

        id_filme_label = tk.Label(self.root, text="ID do Filme:")
        id_filme_entry = tk.Entry(self.root)
        remover_filme_button = tk.Button(self.root, text="Remover Filme", command=lambda: self.handle_remove_film(id_filme_entry.get()))
        id_filme_label.pack()
        id_filme_entry.pack()
        remover_filme_button.pack()
        voltar_button = tk.Button(self.root, text="Voltar", command=self.create_ui)
        voltar_button.pack()

    def create_list_film_widgets(self):
        self.clear_widgets()

        id_filme_label = tk.Label(self.root, text="ID do Filme:")
        id_filme_entry = tk.Entry(self.root)
        listar_filme_button = tk.Button(self.root, text="Listar Filme", command=lambda: self.handle_list_film(id_filme_entry.get()))
        id_filme_label.pack()
        id_filme_entry.pack()
        listar_filme_button.pack()
        voltar_button = tk.Button(self.root, text="Voltar", command=self.create_ui)
        voltar_button.pack()

    def create_list_catalog_widgets(self):
        self.clear_widgets()

        listar_catalogo_button = tk.Button(self.root, text="Listar Catálogo", command=self.list_catalog_func)
        listar_catalogo_button.pack()
        voltar_button = tk.Button(self.root, text="Voltar", command=self.create_ui)
        voltar_button.pack()

    def handle_add_film(self, titulo, diretor, ano, duracao, genero, classificacao, descricao):
        if titulo and diretor and ano and duracao and genero and classificacao and descricao:
            self.add_film_func(titulo, diretor, ano, duracao, genero, classificacao, descricao)
            self.result_label.config(text="Filme cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos")

    def handle_remove_film(self, film_id):
        if film_id:
            self.remove_film_func(film_id)
            self.result_label.config(text="Filme removido com sucesso!")
        else:
            messagebox.showerror("Erro", "Informe o ID do filme")

    def handle_list_film(self, film_id):
        if film_id:
            self.list_film_func(film_id)
        else:
            messagebox.showerror("Erro", "Informe o ID do filme")

    def handle_list_catalog(self):
        self.list_catalog_func()

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            if widget != self.result_label:
                widget.destroy()

    def run(self):
        self.root.mainloop()