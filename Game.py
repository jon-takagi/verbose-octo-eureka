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
from Server_Facing_Networked_Player import Server_Facing_Networked_Player
from Hot_Seat_Player import Hot_Seat_Player
import pickle
import os
class Game():
    default_prefs = [curses.COLOR_BLACK, curses.COLOR_GREEN, curses.COLOR_RED, curses.COLOR_CYAN, 9, 10, 11]
    def __init__(self, map_name=None):
        # self.players = []
        self.world = World()
        self.players = []
        self.set_color_prefs(Game.default_prefs)
        # if map_name == None:
        #     self.map_name = "map1long.png"
        # else:
        if map_name.split(".")[1] == "mfz":
            self.map_name = ""
            self.load_game(map_name)
        else:
            self.map_name = map_name
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
        self.world.capture_stations()
        self.world.scr.refresh()
        curses.noecho()
        print(len(self.players))
        while True:
            for player in self.players:
                player.team.moved_yet = False
                player.team.attacked_yet = False
                player.team.spot_yet = True
            for player in self.players:
                self.update_current_player(player)
                player.send_world_state(pickle.dumps(self.world))
                while not (player.team.has_moved_yet() and player.team.has_attacked_yet()):
                    if self.world.has_winner():
                        self.world.scr.addstr(2, 70, " "*30)
                        self.world.scr.addstr(2, 70, "Game Over")
                        self.world.scr.addstr(3, 70, " "*30)
                        self.world.scr.addstr(3, 70, "Winner is " + str(self.world.get_winner().name))
                        self.world.scr.refresh()
                        break
                    turn = player.get_turn()
                    if self.world.is_valid_turn(turn):
                        if turn.verb == "pass":
                            player.team.moved_yet = True
                            player.team.attacked_yet = True
                        if turn.verb == "mov":
                            player.team.moved_yet = True
                        if turn.verb == "atk":
                            player.team.attacked_yet = True
                            os.system("afplay gunshot.wav")
                        self.update_current_player(player)
                        player.team.do(turn)
                        for p in self.players:
                            p.send_world_state(pickle.dumps(self.world))
                        self.world.scr.refresh()
                    else:
                        self.world.scr.addstr(3, 50, " "*50)
                        self.world.scr.addstr(3, 50, "command forbidden")

        self.world.scr.addstr(25, 50, "game over")
        self.world.scr.getch()
        curses.endwin()
    def update_current_player(self, player):
        # print(player.team.name)
        self.world.scr.addstr(1, 50, " "*50)
        ptn_str = player.team.name + " to "
        if not player.team.has_moved_yet():
            ptn_str += "move"
            if not player.team.has_attacked_yet():
                ptn_str += ", attack"
        elif not player.team.has_attacked_yet():
            ptn_str += "attack"
        self.world.scr.addstr(1, 50, ptn_str)
        self.world.scr.refresh()
    def add_player(self, p):
        # print(">adding player")
        self.players.append(p)
        self.world.add_team(p.team)
    def recieve_world_state(self, world):
        self.world = world
    def load_game(self, file_name):
        self.players = []
        current_team_name = None
        current_team_obj = None
        with open(file_name, "r") as f:
            first_line = f.readline()
            if first_line[0] == "M":
                self.map_name = first_line.split(":")[1].rstrip()

                self.world = World(self.map_name)
                print("creating map from " + self.map_name)
                self.set_color_prefs(Game.default_prefs)
            for line in f:
                # print(line[0])
                if line[0] == "t":
                    current_team_name = line.split("-")[1].split("@")[0]
                    host, port = line.split("-")[1].split("@")[1].split(":")
                    port = int(port)
                    print("creating new team: " + current_team_name)
                    current_team_obj = Team(self.world, current_team_name)
                    self.add_player(Server_Facing_Networked_Player(self, current_team_obj, host, port))
                elif line[0] == "m":
                    loc = location(line.split("@")[1][:-1])
                    current_team_obj.create_mech(line[2:6], loc)
                elif line[0] == "s":
                    loc = location(line.split("@")[1][:-1])
                    self.world.create_station_at(loc, current_team_obj)
