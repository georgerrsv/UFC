from filme import Filme

class Despachante:
    def __init__(self, proxy):
        self.proxy = proxy

    def invoke(self, message):
        parts = message.split()
        if not parts:
            return "Erro: Mensagem vazia"

        operation = parts[0]
        parameters = parts[1:]

        if operation == "adicionarFilme":
            return self.handleAdicionarFilme(parameters)
        elif operation == "removerFilme":
            return self.handleRemoverFilme(parameters)
        elif operation == "exibirDetalhe":
            return self.handleExibirDetalhe(parameters)
        elif operation == "mostrarCatalogo":
            return self.handleMostrarCatalogo(parameters)
        else:
            return "Erro: Operação desconhecida"

    def handleAdicionarFilme(self, parameters):
        if len(parameters) != 7:
            return "Erro: Parâmetros inválidos"
        
        titulo = parameters[0]
        diretor = parameters[1]
        ano = int(parameters[2])
        duracao = int(parameters[3])
        genero = parameters[4]
        classificacao = int(parameters[5])
        descricao = parameters[6]
        filme = Filme(titulo, diretor, ano, duracao, genero, classificacao, descricao)
        response = self.proxy.adicionarFilme(filme)
        return response
    
    def handleRemoverFilme(self, parameters):
        if len(parameters) != 1:
            return "Erro: Parâmetros inválidos"
        response = self.proxy.removerFilme(int(parameters[0]))
        return response
    
    def handleExibirDetalhe(self, parameters):
        if len(parameters) != 1:
            return "Erro: Parâmetros inválidos"
        response = self.proxy.exibirDetalhe(int(parameters[0]))
        return response
    
    def handleMostrarCatalogo(self, parameters):
        if len(parameters) != 0:
            return "Erro: Parâmetros inválidos"
        response = self.proxy.mostrarCatalogo()
        return response