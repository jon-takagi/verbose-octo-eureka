from location import location
from Mech import Mech
from Gadgets import Gadgets
import curses
class Team():
    def __init__(self, world, name):
        self.mechs = []
        self.world = world
        self.name = name
        self.num = 0
        self.moved_yet = False
        self.attacked_yet = False
        self.spot_yet = False
        self.verbs = {"move":Mech.move, "attack":Mech.attack, "spot":Mech.spot}
    def has_moved_yet(self):
        return self.moved_yet
    def has_attacked_yet(self):
        return self.attacked_yet
    def has_spot_yet(self):
        return self.spot_yet
    def add_mech(self, mech):
        self.mechs.append(mech)
    def get_name(self):
        return self.name
    def set_num(self, num):
        self.num = num
    def __str__(self):
        return self.get_name + "contains: " + str(self.mechs)
    def has_lost(self):
        r = False
        for mech in self.mechs:
            r = r or mech.is_active()
        return not r
    def getTurn(self, userInput = None):
        if userInput == None:
            userInput = input(self.name + " to act: ")
        command = userInput[0]
        args = userInput[2:].split(">")
        subject_str = args[0]
        subject_pair = location.move_to_coords(subject_str)
        subject_obj = self.world.table[subject_pair[0]][subject_pair[1]]
        target = args[1]
        print("you orderd the mech at", subject_str, "to", command, "to target", target)
        subject_obj.__class__ = Mech
        subject_obj.do(command, target)
    def do_parsed(self, subject, verb, target):
        if subject in self.mechs:
            if verb in self.verbs:
                print("mech at " + str(subject.location) + " is " + str(self.verbs[verb].__name__) +"-ing to " + str(target.location))
                subject.verbs[verb](target)
    def do(self, command):
        words = command.split(" ")
        subj = self.world.at(words[0])
        verb = words[1]
        target = self.world.at(words[2])
        self.do_parsed(subj, verb, target)
    def create_mech(self, equipment_str,loc = location(0,0)):
        mech = Mech(self.world, Gadgets(equipment_str), loc, self)
        self.add_mech(mech)
        return mech
