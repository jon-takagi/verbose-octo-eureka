import random
import time
import socket
from Turn import Turn
from Player import Player
class Server_Facing_Networked_Player(Player):
    def __init__(self, game, team):
        super().__init__(game,team)
        self.ready_to_get_state = False
    def get_turn(self):
        host = "localhost"
        port = 42069
        s = socket.socket()
        s.connect((host, port))
        s.send("send turn".encode('ascii'))
        msg = s.recv(1024)
        return msg.decode()
    def send_world_state(self, world_state):
        host = "localhost"
        port = 42069
        s = socket.socket()
        s.connect((host, port))
        s.send(("recieve world_state" + ":" + str(len(world_state))).encode('ascii'))
        msg = s.recv(1024)
        if msg.decode() == "ready":
            print("sending world state")
            s.send(str(world_state).encode('ascii'))
            print("finished sending")
