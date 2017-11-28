from tile_content import tile_content
from location import location
from location_helpers import move_to_coords
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

scr = curses.initscr()
curses.start_color()
# curses.use_default_colors()
for i in range(1, curses.COLORS):
    curses.init_pair(i, i, curses.COLOR_BLACK)
scr.keypad(1)
curses.mousemask(curses.ALL_MOUSE_EVENTS)
curses.init_pair(1, curses.COLOR_BLACK, 255)
scr.bkgd(" ", curses.color_pair(0))

w = World("map1long.png", scr)
jets = Team(w, "Jets")
sharks = Team(w, "Sharks")
jets_queen = Mech(w, Gadgets(Gadget("atk"),Gadget("spt"),Gadget("mov"), Gadget("mov")), location("G6"), jets)
sharks_b1 = Mech(w, Gadgets(Gadget("atk"),Gadget("atk"),Gadget("mov"), Gadget("mov")), location("N24"), sharks)
jets.add_mech(jets_queen)
sharks.add_mech(sharks_b1)
w.add_team(sharks)
w.add_team(jets)
for i in range(1, curses.COLORS):
    curses.init_pair(i, i, curses.COLOR_BLACK)
for i in range(1, 255):
    scr.addstr(str(i) + u"\u2588", curses.color_pair(i))
# w.curses_display_table()
scr.addstr("\n")
scr.addstr("jets team #: " + str(jets.num))
scr.getch()
