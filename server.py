import socket
import threading

class SocketServer:
    """A socket server to host socket clients"""

    def __init__(self, port = 5050, host = None, header = 64, encode_format = 'utf-8', disconnect_code = '!!DISCONNECT!!'):
        self.port = port
        self.host = host if host else socket.gethostbyname(socket.gethostname())
        self.header = header
        self.encode_format = encode_format
        self.disconnect_code = disconnect_code
        self.addr = (self.host, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def handle_client(self, conn, addr):
        """Handle a new client joining the server"""
        print(f'[[NEW CONNECTION]] {addr} connected')
        while 1:
            msg_length = conn.recv(self.header).decode(self.encode_format)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.encode_format)
                if msg == self.disconnect_code:
                    break
                print(f'\t[[{addr}]] {msg}')

    def start(self):
        """Start running the server"""
        self.socket.bind(self.addr)
        self.socket.listen()
        print(f'[[LISTENING]] server is listening on {self.host}')
        while 1:
            conn, addr = self.socket.accept()
            threading.Thread(target = self.handle_client, args = (conn, addr)).start()
            print(f'[[Active connections]] {threading.activeCount() - 1}')

if __name__ == "__main__": # driver code
    server = SocketServer()
    print('[[STARTING]] the server is starting')
    server.start()
