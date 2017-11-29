from location import location
import re
class Turn():
    def __init__(self, command, owner):
        self.owner = owner
        self.subj = None
        self.verb = None
        self.target = None
        targeted_commands = r"[a-zA-V]\d+ (mov|atk|spt|inf) [a-zA-V]\d+"
        info_command = r"info [a-zA-V]\d{1,2}"
        if type(command) == type(b'a'):
            command = command.decode('ascii')
        if command == "pass":
            #self.subj = None
            self.verb = "pass"
            #self.target = None
        elif re.search(info_command, command) != None:
            #command is of the form
            #info a1
            #info z31
            #info A1
            #info V31
            words = command.split(" ")
            self.verb = "inf"
            self.subj = location(words[1])
            #self.target = None
        elif re.search(targeted_commands, command) != None:
            #command is targeted
            #a1 atk A1
            #V31 mov a1
            words = command.split(" ")
            self.subj = location(words[0])
            self.verb = words[1]
            self.target = location(words[2])
    def get_subj_loc(self):
        return self.subj
    def get_verb(self):
        return self.verb
    def get_target_loc(self):
        return self.target
    def is_valid(self):
        return False
