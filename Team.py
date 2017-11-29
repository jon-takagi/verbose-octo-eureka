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
        self.spot_yet = True
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
    def get_active_mechs(self):
        active_mechs = []
        for mech in self.mechs:
            if mech.is_active():
                active_mechs.append(mech)
        return active_mechs
    def set_num(self, num):
        self.num = num
    def __repr__(self):
        return self.get_name() + " " + str(self.mechs)
    def has_lost(self):
        return len(self.get_active_mechs()) == 0
    def do(self, turn):
        if turn.get_target_loc() is None:
            turn.target = location("n0")
        if turn.verb == "pass":
            self.end_turn()
            return
        m = self.world.at(turn.get_subj_loc())
        if not m.prepped:
            m.prep()
        self.world.verbs[turn.verb](m, turn.get_target_loc())
    def create_mech(self, equipment_str,loc = location(0,0)):
        mech = Mech(self.world, Gadgets(equipment_str), loc, self)
        self.world.settile(mech, loc.row, loc.col)
        self.add_mech(mech)
        return mech
    def end_turn(self):
        self.moved_yet = True
        self.attacked_yet = True
        self.spot_yet = True
