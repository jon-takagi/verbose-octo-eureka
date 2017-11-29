from Team import Team
import curses
class Player():
    def __init__(self, game, team):
        self.team = team
        self.game = game
        self.moved = False
        self.attacked = False
    def get_turn(self):
        pass
    def has_moved(self):
        return self.moved
    def has_attacked(self):
        return self.attacked
