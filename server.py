import socket
import threading

class SocketServer:
    """A socket server to host socket clients"""

    def __init__(self, port = 5050, host = None):
        self.port = port
        self.host = socket.gethostbyname(socket.gethostname()) if host is None else host
        self.addr = (self.host, self.port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.addr)

    def handle_client(self, conn, addr):
        """Handle a new client joining the server"""
        print(f'[[NEW CONNECTION]] {addr} connected')
        connected = True
        while connected:
            msg = conn.recv()

    def start(self):
        """Star running the server"""
        self.server.listen()
        while 1:
            conn, addr = self.server.accept()
            threading.Thread(target = self.handle_client, args = (conn, addr)).start()
            print(f'[[Active connections]] {threading.activeCount() - 1}')

if __name__ == "__main__": # driver code
    server = SocketServer()
    print('[[STARTING]] the server is starting')
    server.start()
