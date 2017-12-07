import random
import time
import socket
from Turn import Turn
class Networked_Player_Front():
    def __init__(self, name):
        self.name = name
    def get_turn(self):
        host = "localhost"
        port = 42069
        s = socket.socket()
        s.connect((host, port))
        s.send("send turn".encode('ascii'))
        msg = s.recv(1024)
        return self.name + ": " + msg.decode()
