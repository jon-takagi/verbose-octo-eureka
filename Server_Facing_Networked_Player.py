import random
import time
import socket
from Turn import Turn
from Player import Player
class Server_Facing_Networked_Player(Player):
    def __init__(self, game, team, host="localhost", port=42069):
        super().__init__(game,team)
        self.ready_to_get_state = False
        self.s = socket.socket()
        self.s.connect((host, port))
    def get_turn(self):
        self.s.send("send turn".encode('ascii'))
        command = self.s.recv(1024).decode('ascii')
        while True:
            if self.is_malformed(command):
                command = self.check_input()
                self.malformed_input()
            else:
                self.reset_input(command)
                return Turn(command, self.team)
    def send_world_state(self, world_state):
        self.s.send(("recieve world_state" + ":" + str(len(world_state))).encode('ascii'))
        msg = self.s.recv(1024)
        if msg.decode() == "ready":
            self.s.send(world_state)
            msg = self.s.recv(1024).decode("ascii")
            if msg == "done":
                return
