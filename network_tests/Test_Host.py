import socket
class Test_Host():
    def __init__(self):
        self.players = []
    def start(self):
        while True:
            for player in self.players:
                turn = player.get_turn()
                while not self.is_valid(turn):
                    turn = player.get_turn()
                self.do(turn)
    def is_valid(self, turn):
        return True
    def do(self, turn):
        print(turn)
    def add_player(self, player):
        self.players.append(player)
