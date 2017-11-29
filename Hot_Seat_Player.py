from Player import Player
from Mech import Mech
from location_helpers import str_to_coords
from location_helpers import coords_to_str
from Turn import Turn
import curses
import re
class Hot_Seat_Player(Player):
    MAX_COMMAND_LENGTH = 11
    def __init__(self, game, team):
        super().__init__(game,team)
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
        #line 2 is the input for a command to be issued
        curses.noecho()
        scr.addstr(3, 50, " "*50)
        scr.addstr(3, 50, command)
        #line 3 is the last command issued
        scr.addstr(2, 50, " "*11)
        targeted_commands = r"[a-zA-V]\d+ (mov|atk|spt|inf) [a-zA-V]\d+"
        #this pattern matches commands of the form
        #subject.mov OR atk OR spt (target)
        if str(command).strip()[2:-1] == "q":
            curses.endwin()
        if str(command).strip()[2:-1] == "pass":
        #curses.getch() returns a bytes object.
        #str(command) returns b'blahblahblah'. str(command)[2:-1] slices b' and ' off
            self.team.moved_yet = True
            self.team.attacked_yet = True
            self.team.spot_yet = True
            return
        if re.search(targeted_commands, str(command)) != None:
            return Turn(str(command), self.team)
