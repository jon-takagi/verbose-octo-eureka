import random
from Gadget import Gadget
import Gadgets
from tile_content import tile_content
from location import location
from Cover import Cover
class Mech(tile_content):
    BASE_MOVEMENT = 1
    def d6(self):
        return random.randint(1,6)
    def d8(self):
        return random.randint(1,8)
    def twoD6(self):
        return self.d6() +  self.d6()
    def __init__(self, world, gadgets, location, team):
        self.team = team
        self.gadgets = gadgets
        self.gadgets.update_count()
        self.location = location
        self.world = world
        self.world.table[location.row][location.col] = self
        # self.movement_range = calculateMovement()
        self.scores = {"atk":0,"def":0,"mov":0,"spt":0}
        self.active = True
        self.prepped = False
        self.atk_range = 8
        self.nearby_cover = []
    def is_prepped(self):
        return self.prepped
    def is_active(self):
        return self.active
    def take_damage(self, damage):
        if not self.gadgets.has_active():
            self.active = False
            return
        if damage > 0:
            if self.gadgets.has_active():
                dmg = random.randint(0,len(self.gadgets.members)-1)
                while not self.gadgets.members[dmg].active:
                    dmg = random.randint(0,len(self.gadgets.members)-1)
                self.gadgets.members[dmg].active = False
                self.gadgets.update_count()
                self.take_damage(damage - 1)
            else:
                self.active = False
    def get_scores(self):
        self.prep()
        s = ""
        for score in self.scores:
            s += score + ": " + str(self.scores[score]) + " "
        return s
    def reset_scores(self):
        self.scores = {"atk":0,"def":0,"mov":0,"spt":0}
    def prep_atk(self):
        if self.gadgets.count["atk"] == 2:
            self.scores["atk"] = self.d8() + self.twoD6()
        else:
            self.scores["atk"] = self.twoD6() * self.gadgets.count["atk"]
    def prep_def(self):
        self.scores["def"] = 0
        for i in range(self.gadgets.count["def"]):
            self.scores["def"] += self.d6()
    def prep_mov(self):
        self.scores["mov"] = 0
        for i in range(self.gadgets.count["mov"]):
            self.scores["mov"] += self.d6()
    def prep_spt(self):
        for i in range(self.gadgets.count["spt"]):
            self.scores["spt"] += self.d6()
    def prep(self):
        if not self.is_prepped():
            self.reset_scores
            self.prep_atk()
            self.prep_def()
            self.prep_mov()
            self.prep_spt()
            self.prepped = True
    def valid_move_tiles(self):
        if self.gadgets.count["mov"] == 2:
            return self.world.list_tiles_in_range(self.location, self.scores["mov"])
        else:
            return self.world.list_walkable_tiles_in_range(self.location, self.scores["mov"])
    def move(self,target):
        if True: #replace with check to see if target is within move range
            self.set_location(target)
        self.world.curses_display_table()
    def can_move_to(self, target):
        return target in self.valid_atk_tiles()
    def set_location(self, target):
        self.world.table[self.location.row][self.location.col] = tile_content()
        self.location = target
        self.world.table[target.row][target.col] = self
        self.update_nearby_cover()

    def valid_atk_tiles(self):
        return self.world.list_tiles_in_range(self.location, self.atk_range)
    def can_attack(self, target):
        return target in self.valid_atk_tiles()
    def attack(self, target):
        # self.world.window.addstr(6,50, self.short_specs() + " is attacking " + target.short_specs())
        if isinstance(target, location):
            target = self.world.at(target)
        if isinstance(target, Mech):
            if not target.is_prepped():
                target.prep()
            self.world.scr.addstr(7,50, " " *50)
            self.world.scr.addstr(7,50, self.short_specs() + " is attacking " + target.short_specs())
            hits = max(self.scores["atk"] + target.scores["spt"] - target.scores["def"],0)
            self.world.scr.addstr(8,50, " " * 50)
            self.world.scr.addstr(8,50, "scored " + str(hits) + " hits")
            dmg_to_take = 0
            for hit in range(hits-1):
                hit_score = self.d6()
                if target.is_in_cover():
                    if hit_score == 6:
                        target.take_damage(1)
                        dmg_to_take += 1
                    else:
                        if hit_score == 5 or hit_score == 4:
                            self.world.at(target.get_nearby_cover()[random.randint(0,len(target.get_nearby_cover()))-1 ]).height -= 1
                else: #target_mech is not in cover
                    if hit_score == 6 or hit_score == 5:
                        target.take_damage(1)
                        dmg_to_take += 1
            # target.take_damage(dmg_to_take)
            self.world.scr.addstr(9,50, " "*50)
            self.world.scr.addstr(9,50, "dealt " + str(dmg_to_take) + " dmg")
            self.world.curses_display_table()
            # if hit_score >= roll_above_to_damage:
    def spot(self, target):
        print("spotting mech at " + str(target))
    def __str__(self):
        def match(x1, x2):
            c1 = {}
            c2 = {}
            for x in x1:
                if x in c1:
                    c1[x] += 1
                else:
                    c1[x] = 1
            for x in x2:
                if x in c2:
                    c2[x] += 1
                else:
                    c2[x] = 1
            return c1 == c2

        pawn = ["atk", "spt", "def", "mov"] #RYBG
        knight = ["atk", "mov",'mov',"def"] #RGGB
        bishop = ["atk", "atk","mov","mov"] #RRGG
        rook = ["atk","atk","def","def"] #RRBB
        queen = ["atk","mov","spt","mov"] #RBYB
        king = ["spt","spt","def","def"] #YYBB
        keys = [pawn, knight, bishop, rook, queen, king]
        black_chars = ["\u265F","\u265E","\u265D","\u265C","\u265B","\u265A"]
        white_chars = ["\u2659","\u2658","\u2657","\u2656","\u2655","\u2654"]
        for i in range(len(keys)):
            if match(self.gadgets.as_string_arr(),keys[i]):
                if self.active:
                    return black_chars[i]
                else:
                    return white_chars[i]
        else:
            return "#"
    def short_specs(self):
        return self.team.name + " " + str(self.location)
    def __repr__(self):
        specs = ""
        dice = {"atk":"R", "def":"B", "mov":"G", "spt":"Y"}
        for gadget in self.gadgets.members:
            specs += dice[gadget.kind] if gadget.is_active() else dice[gadget.kind].lower()
        return specs + " @ " + str(self.location)
    def get_specs(self):
        specs = self.team.name + " "
        dice = {"atk":"R", "def":"B", "mov":"G", "spt":"Y"}
        for gadget in self.gadgets.members:
            specs += dice[gadget.kind] if gadget.is_active() else dice[gadget.kind].lower()
        specs += " @ "+ str(self.location)
        specs += " NOT " if not self.is_in_cover() else " "
        specs += "in cover"
        return specs
    def update_nearby_cover(self):
        self.nearby_cover = []
        for tile in self.location.neighbors():
            if isinstance(self.world.at(tile), Cover):
                self.nearby_cover.append(tile)
    def get_nearby_cover(self):
        return self.nearby_cover
    def is_in_cover(self):
        self.update_nearby_cover()
        return len(self.nearby_cover) > 0



# soldier = Mech(Gadgets.soldier_kit, location(0,0), "barrett's privateers")
