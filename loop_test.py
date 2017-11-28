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
scr.keypad(1)
curses.mousemask(curses.ALL_MOUSE_EVENTS)
curses.init_pair(1, curses.COLOR_BLACK, 255)
scr.bkgd(" ", curses.color_pair(0))
w = World("map1long.png", scr)
# w = World("tile_test.png", scr)
jets = Team(w, "Jets", "#0000FF")
sharks = Team(w, "Sharks", "#009933")

jets_queen = Mech(w, Gadgets(Gadget("atk"),Gadget("spt"),Gadget("mov"), Gadget("mov")), location("G6"), jets)
sharks_b1 = Mech(w, Gadgets(Gadget("atk"),Gadget("atk"),Gadget("mov"), Gadget("mov")), location("N24"), sharks)
sharks_b2 = Mech(w, Gadgets(Gadget("atk"),Gadget("atk"),Gadget("mov"), Gadget("mov")), location("B9"), sharks)
jets.add_mech(jets_queen)
sharks.add_mech(sharks_b1)
sharks.add_mech(sharks_b2)
w.add_team(sharks)
w.add_team(jets)

# curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
# curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

w.curses_display_table()
player_index = 0

current_player = w.teams[player_index % len(w.teams)]
scr.addstr(1, 50, current_player.name)
while not w.game_over():
    event = scr.getch()
    if event == ord("q"): break
    if event == curses.KEY_MOUSE:
        w.curses_display_table()
        _, mx, my, _, mstate = curses.getmouse()
        y, x = scr.getyx()
        selected_mech = None
        if mstate == curses.BUTTON1_CLICKED:
            if isinstance(w.table[my][mx], Mech):
                m = w.table[my][mx]
                scr.addstr(2,50, " "*50)
                scr.addstr(3,50, " "*50)
                scr.addstr(2,50, m.get_specs())
                scr.addstr(3,50, m.get_scores())
                for tile in m.valid_move_tiles():
                    scr.addstr(tile.row, tile.col, str(w.table[tile.row][tile.col]), curses.color_pair(w.move_radius_color_pair_num))
        if mstate == curses.BUTTON1_PRESSED and not current_player.moved_yet:
            w.down_at = location(my,mx)
            if isinstance(w.at(w.down_at),Mech):
                selected_mech = w.at(w.down_at)
            scr.addstr(4, 50, " "*28)
            scr.addstr(5, 50, " "*28)
            scr.addstr(4, 50, "m1 d " + "@ \"" + coords_to_str((my,mx)) + "\"")
        if mstate == curses.BUTTON1_RELEASED:
            scr.addstr(5, 50, " "*28)
            current_player.moved_yet = True
            if selected_mech != None:
                current_player.do(selected_mech, "move", location(my, mx))
            scr.addstr(5, 50, "m1 u " + "@ \"" + coords_to_str((my,mx)) + "\"")
        if mstate == curses.BUTTON3_PRESSED and not current_player.attacked_yet:
            w.down_at = location(my,mx)
            if isinstance(w.at(w.down_at),Mech):
                selected_mech = w.at(w.down_at)
            scr.addstr(4, 50, " "*28)
            scr.addstr(5, 50, " "*28)
            scr.addstr(4, 50, "m2 d " + "@ \"" + coords_to_str((my,mx)) + "\"")
        if mstate == curses.BUTTON3_RELEASED:
            current_player.attacked_yet = True
            if selected_mech != None:
                current_player.do(selected_mech, "attack", location(my, mx))
            scr.addstr(5, 50, " "*28)
            scr.addstr(5, 50, "m2 u " + "@ \"" + coords_to_str((my,mx)) + "\"")
    if current_player.moved_yet and current_player.attacked_yet:
        player_index += 1
        current_player.moved_yet = False
        current_player.attacked_yet = False
        current_player = w.teams[player_index % len(w.teams)]
        scr.addstr(1, 50, " "*28)
        scr.addstr(1, 50, current_player.name)
    scr.refresh()
curses.endwin()
