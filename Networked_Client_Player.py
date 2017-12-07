from Player import Player
from Mech import Mech
from location_helpers import str_to_coords
from location_helpers import coords_to_str
from Turn import Turn
import curses
class Hot_Seat_Player(Player):
    MAX_COMMAND_LENGTH = 11
    def __init__(self, host):
        self.host = host
    def get_turn(self):
        w = self.game.world
        scr = w.scr
        mechs = self.team.world.get_all_mechs()
        for i in range(len(mechs)):
            scr.addstr(i + 11, 50, " "*50)
            scr.addstr(i + 11, 50, mechs[i].get_specs())
        curses.echo()
        scr.move(2, 50)
        command = scr.getstr(2, 50, Hot_Seat_Player.MAX_COMMAND_LENGTH)
        scr.addstr(2, 50, " "*11)
        #line 2 is the input for a command to be issued
        curses.noecho()
        scr.addstr(3, 50, " "*50)
        scr.addstr(3, 50, command)
        #line 3 is the last command issued
        
        return Turn(command, self.team)
