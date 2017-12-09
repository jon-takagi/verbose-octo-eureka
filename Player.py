from Team import Team
import curses
import re
from Mech import Mech
from location_helpers import str_to_coords
from location_helpers import coords_to_str
from Turn import Turn
import curses
import re
class Player():
    MAX_COMMAND_LENGTH = 11
    def __init__(self, game, team):
        self.team = team
        self.game = game
        self.moved = False
        self.attacked = False
    def get_turn(self):
        command = self.check_input()
        while True:
            if self.is_malformed(command):
                command = self.check_input()
                self.malformed_input()
            else:
                self.reset_input(command)
                return Turn(command, self.team)
    def has_moved(self):
        return self.moved
    def has_attacked(self):
        return self.attacked
    def send_world_state(self, state):
        pass
    def is_malformed(self,command):
        # print(command == "pass")
        targeted_commands = r"[a-zA-V]\d+ (mov|atk|spt|inf) [a-zA-V]\d+"
        info_command = r"info [a-zA-V]\d{1,2}"
        return not(command == "help" or command == "pass" or re.search(info_command, command) != None or re.search(targeted_commands, command) != None)

    def check_input(self):
        #This method should return the user input as a string
        pass


    def malformed_input(self):
        #this method should inform the user that their input was malformed
        pass

    def reset_input(self, commmand):
        #This method should reset the user input method, preparing it for the next call of check_input()
        #erase the line in curses
        #don't do anything in a terminal
        #does NOT prompt for another input
        pass
