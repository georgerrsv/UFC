class Proxy:
    def __init__(self, udp_client):
        self.udp_client = udp_client

    def adicionarFilme(self, filme):
        request = f"adicionarFilme {filme.to_json()}"
        response = self.udp_client.sendRequest(request)
        return response
    
    def removerFilme(self, id):
        request = f"removerFilme {id}"
        response = self.udp_client.sendRequest(request)
        return response
    
    def exibirDetalhe(self, id):
        request = f"exibirDetalhe {id}"
        response = self.udp_client.sendRequest(request)
        return response
    
    def mostrarCatalogo(self):
        request = "mostrarCatalogo"
        response = self.udp_client.sendRequest(request)
        return response