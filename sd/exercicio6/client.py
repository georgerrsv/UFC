from proxy import Proxy
from handle_client import handle_client
from tcp_client import TCPClient

if __name__ == "__main__":
    host = 'localhost'
    port = 12345

    client = TCPClient(host, port)
    proxy = Proxy(client)

    handle_client(proxy)

    client.close()