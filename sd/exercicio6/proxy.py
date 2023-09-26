class Proxy:
    def __init__(self, client):
        self.client = client

    def invoke(self, method_name, *args):
        request = {'method': method_name, 'args': args}
        self.client.sendRequest(request)
        response = self.client.getResponse()
        return response
    
    def close(self):
        self.client.close()