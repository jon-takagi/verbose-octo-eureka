from tile_content import tile_content
from location import location
from location_helpers import move_to_coords
from location_helpers import coords_to_str
from location_helpers import distance_between
from Gadgets import Gadgets
import random
from Gadget import Gadget
from Cover import Cover
from Mech import Mech
from PIL import Image
from Team import Team
from World import World
import curses

scr = curses.initscr()
curses.start_color()
w = World("map1long.png")
w.testing = True
# w = World("tile_test.png", scr)
jets = Team(w, "Jets", curses.COLOR_RED)
sharks = Team(w, "Sharks", curses.COLOR_GREEN)
queen = Mech(w, Gadgets(Gadget("atk"),Gadget("def"),Gadget("mov"), Gadget("mov")), location("G6"), jets)
b1 =    Mech(w, Gadgets(Gadget("atk"),Gadget("atk"),Gadget("mov"), Gadget("mov")), location("N24"), sharks)
b2 = Mech(w, Gadgets(Gadget("atk"),Gadget("atk"),Gadget("mov"), Gadget("mov")), location("B9"), sharks)
jets.add_mech(queen)
sharks.add_mech(b1)
sharks.add_mech(b2)
w.add_team(sharks)
w.add_team(jets)
