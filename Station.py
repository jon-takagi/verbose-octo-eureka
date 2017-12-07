from tile_content import tile_content
from location import location
from Mech import Mech
class Station(tile_content):
    def __init__(self, world, loc, owner = None):
        self.world = world
        self.location = loc
        self.owner = owner
    def __str__(self):
        if self.owner == None:
            return u"\u2616"
        else:
            return u"\u2617"
    def captured_by(self, team):
        self.owner = owner
    def get_owner_color_pair_num(self):
        if self.owner == None:
            return 0
        else:
            return self.owner.num
    def nearby_mechs(self):
        mechs = []
        string = ""
        for loc in self.location.neighbors():
            if isinstance(self.world.at(loc), Mech):
                mechs.append(self.world.at(loc))
            string += str(self.world.at(loc))
            string += " @ " + loc.as_str() + "; "
        if self.location == location("u2"):
            self.world.scr.addstr(20, 50, str(len(mechs)) + " mechs nearby " + str(self.location))
            self.world.scr.addstr(21, 50, " "*50)
            self.world.scr.addstr(21, 50, str(mechs))
            self.world.scr.addstr(22, 50, " "*50)
            self.world.scr.addstr(22, 50, str(string))
        return mechs
    def update_owner(self):
        nm = self.nearby_mechs()
        # print(self.location, ":", self.is_captured())
        if len(nm) == 1:
            self.owner = nm[0].team
