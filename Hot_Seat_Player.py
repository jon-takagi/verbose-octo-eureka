from Player import Player
from Mech import Mech
from location_helpers import str_to_coords
from location_helpers import coords_to_str
from Turn import Turn
import curses
import re
class Hot_Seat_Player(Player):
    MAX_COMMAND_LENGTH = 11
    def get_turn(self):
        self.game.world.list_mechs()
        turn = super().get_turn()
        self.game.world.list_mechs()
        return turn
    def check_input(self):
        curses.echo()
        self.game.world.scr.move(2, 50)
        command = self.game.world.scr.getstr(2, 50, Hot_Seat_Player.MAX_COMMAND_LENGTH)
        return command.decode('ascii')

    def malformed_input(self):
        self.game.world.scr.addstr(2, 50, " "*11)
        #line 2 is the input for a command to be issued
        curses.noecho()
        self.game.world.scr.addstr(3, 50, " "*50)
        self.game.world.scr.addstr(3, 50, "input malformed")

    def reset_input(self, commmand):
        self.game.world.scr.addstr(2, 50, " "*11)
        #line 2 is the input for a command to be issued
        curses.noecho()
        self.game.world.scr.addstr(3, 50, " "*50)
        self.game.world.scr.addstr(3, 50, str(commmand))
