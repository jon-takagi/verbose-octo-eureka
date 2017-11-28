from Player import Player
import curses
class Hot_Seat_Player(Player):
    def __init__(self, game, team):
        super().__init__(game,team)
    def get_turn(self):
        event = self.game.world.scr.getch()
        if event == curses.KEY_ENTER or event == 10 or event == "\n":
            return "f5 move A10"
