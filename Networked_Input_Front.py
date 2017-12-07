from Player import Player
from Mech import Mech
from location_helpers import str_to_coords
from location_helpers import coords_to_str
from Turn import Turn
import curses

class Networked_Input_Front(Player):
    def __init__(self, game, team, host="localhost", port=42069):
        super().__init__(game, team)
        self.host = ip
        self.port = port
    def get_turn(self):
        port = 42069
        s = socket.socket()
        s.connect((self.host, self.port))
        s.send("send turn".encode('ascii'))
        msg = s.recv(1024)
        return msg.decode()
