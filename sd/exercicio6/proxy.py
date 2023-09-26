class Proxy:
    def __init__(self, client):
        self.client = client

    def invoke_remote(self, method_name, *args):
        request = {'method': method_name, 'args': args}
        self.client.send_request(request)
        response = self.client.get_response()
        return response
