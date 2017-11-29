from tile_content import tile_content
from location import location
from location_helpers import str_to_coords
from location_helpers import coords_to_str
from location_helpers import distance_between
from Gadgets import Gadgets
import random
from Cover import Cover
from Mech import Mech
from PIL import Image
from Team import Team
from World import World
import curses
from Gadget import Gadget
from Window import Window
from Player import Player
from Hot_Seat_Player import Hot_Seat_Player
class Game():
    default_prefs = [curses.COLOR_BLACK, curses.COLOR_GREEN, curses.COLOR_RED, curses.COLOR_CYAN, 9, 10, 11]
    def __init__(self, mapname=None):
        if mapname == None:
            mapname = "map1long.png"
        self.players = []
        self.world = World(mapname)
        self.set_color_prefs(Game.default_prefs)
    def set_color_prefs(self, prefs):
        #prefs is an array
# background, move radius color, attack radius color, cover background color, MOVE_RADIUS_COLOR_PAIR_NUM, ATTACK_RANGE_COLOR_PAIR_NUM, COVER_COLOR_PAIR_NUM
#      0    ,       1          ,           2        ,           3           ,              4            ,               5            ,         6
        curses.init_pair(prefs[6], prefs[0], prefs[3])
        curses.init_pair(prefs[4], prefs[1], prefs[0])
        curses.init_pair(prefs[5], prefs[2], prefs[0])
        self.world.MOVE_RADIUS_COLOR_PAIR_NUM = prefs[4]
        self.world.ATTACK_RANGE_COLOR_PAIR_NUM = prefs[5]
        self.world.COVER_COLOR_PAIR_NUM = prefs[6]
    def start(self):
        self.world.curses_display_table()
        self.world.scr.refresh()
        curses.noecho()
        while not self.world.has_winner():
            for player in self.players:
                player.team.moved_yet = False
                player.team.attacked_yet = False
                player.team.spot_yet = False
            for player in self.players:
                while not (player.team.has_moved_yet() and player.team.has_attacked_yet() and player.team.has_spot_yet()):
                    self.world.scr.addstr(1, 50, " "*50)
                    ptn_str = player.team.name + " to "
                    if not player.team.has_moved_yet():
                        ptn_str += "move"
                        if not player.team.has_attacked_yet():
                            ptn_str += ", attack"
                    elif not player.team.has_attacked_yet():
                        ptn_str += "attack"
                    self.world.scr.addstr(1, 50, ptn_str)
                    turn = player.get_turn()
                    if self.world.is_valid_turn(turn):
                        if turn.verb == "mov":
                            player.team.moved_yet = True
                        if turn.verb == "atk":
                            player.team.attacked_yet = True
                        if turn.verb == "spt":
                            player.team.spot_yet = True
                        player.team.do(turn)
                        self.world.scr.refresh()
                print(">?")
        # curses.endwin()
        # return self.world.active_teams()[0].name
    def add_player(self, p):
        self.players.append(p)
    def load_game(self, file_name):
        current_team_name = None
        current_team_obj = None
        with open(file_name, "r") as f:
            for line in f:
                if line[0] == "t":
                    current_team_name = line[2:-1]
                    # print("creating new team: " + current_team_name)
                    current_team_obj = Team(self.world, current_team_name)
                    self.add_player(Hot_Seat_Player(self, current_team_obj))
                    self.world.add_team(current_team_obj)
                elif line[0] == "m":
                    loc = location(line.split("@")[1][:-1])
                    # print("creating " + current_team + " mech: " + line[2:6] + " at " + location)
                    current_team_obj.create_mech(line[2:6], loc)
