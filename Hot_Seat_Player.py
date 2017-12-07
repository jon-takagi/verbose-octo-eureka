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
        w = self.game.world
        self.scr = w.scr
        mechs = self.team.world.get_all_mechs()
        for i in range(len(mechs)):
            self.scr.addstr(i + 11, 50, " "*50)
            self.scr.addstr(i + 11, 50, mechs[i].get_specs())
        command = self.check_input()
        while True:
            # print(self.is_malformed(command))
            if self.is_malformed(command):
                command = self.check_input()
                self.malformed_input()
            else:
                self.reset_input(command)
                return Turn(command, self.team)

        for i in range(len(mechs)):
            self.scr.addstr(i + 11, 50, " "*50)
            self.scr.addstr(i + 11, 50, mechs[i].get_specs())
    def is_malformed(self,command):
        # print(command == "pass")
        targeted_commands = r"[a-zA-V]\d+ (mov|atk|spt|inf) [a-zA-V]\d+"
        info_command = r"info [a-zA-V]\d{1,2}"
        return not(command == "help" or command == "pass" or re.search(info_command, command) != None or re.search(targeted_commands, command) != None)
    def check_input(self):
        curses.echo()
        self.scr.move(2, 50)
        command = self.scr.getstr(2, 50, Hot_Seat_Player.MAX_COMMAND_LENGTH)
        return command.decode('ascii')
    def malformed_input(self):
        self.scr.addstr(2, 50, " "*11)
        #line 2 is the input for a command to be issued
        curses.noecho()
        self.scr.addstr(3, 50, " "*50)
        self.scr.addstr(3, 50, "input malformed")

    def reset_input(self, commmand):
        self.scr.addstr(2, 50, " "*11)
        #line 2 is the input for a command to be issued
        curses.noecho()
        self.scr.addstr(3, 50, " "*50)
        self.scr.addstr(3, 50, str(commmand))
