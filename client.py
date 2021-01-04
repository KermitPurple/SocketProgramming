import socket
import threading
from server import SocketServer

class SocketClient(SocketServer):
    """A socket client to connect to a socket server"""

    def connect(self):
        """Connect to the server"""
        self.socket.connect(self.addr)

    def disconnect(self):
        """Disconnect from the server"""
        self.send(self.disconnect_code)

    def send(self, msg):
        """Send a message to the server"""
        msg = msg.encode(self.encode_format)
        msg_length = len(msg)
        msg_length = str(msg_length).encode(self.encode_format)
        msg_length += b' ' * (self.header - len(msg_length))
        self.socket.send(msg_length)
        self.socket.send(msg)

if __name__ == "__main__": # driver code
    client = SocketClient()
    client.connect()
    client.send('This works!')
    client.send(input('Enter a message to send> '))
    client.disconnect()
