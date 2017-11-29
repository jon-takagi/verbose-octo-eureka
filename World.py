from tile_content import tile_content
from location import location
import Gadgets
import curses
from queue import Queue
from Cover import Cover
from Mech import Mech
from PIL import Image
from Team import Team
from td import Dimesions
from location_helpers import str_to_coords
from location_helpers import coords_to_str
from location_helpers import distance_between
# from td import TABLE_HEIGHT
class World():
    def none():
        pass

    def __init__(self,mapName, window=None):
        self.table = self.gen_table(mapName)
        self.teams = []
        self.scr = curses.initscr()
        self.scr.keypad(1)
        curses.mousemask(curses.ALL_MOUSE_EVENTS)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, 255)
        self.scr.bkgd(" ", curses.color_pair(0))
        self.down_at = None
        self.selected_mech = None
    def gen_table(self, mapName):
        table = [[tile_content() for i in range(Dimesions.TABLE_WIDTH)] for j in range(Dimesions.TABLE_HEIGHT)]
        img = Image.open(mapName)
        pixels = img.load()
        for j in range(img.size[1]):
            for i in range(img.size[0]):
                p = pixels[i,j]
                content = "\u00B7"
                if isinstance(p, tuple):
                    if p[0] <= 128:
                        content = Cover(int((256-p[0])/32))
                    if p[0] >= 255:
                        content = tile_content()
                table[i][j] = content
        return table
    def settile(self,val, row,col=None):
        if col == None:
            cord = move_to_coords(row)
            row = cord[0]
            col = cord[1]
        self.table[row][col] = val
    def at(self,l):
        if type(l) != location:
            l = location(l)
        return self.table[l.row][l.col]

    def info(mech, loc):
        mech.world.curses_display_table()
        mech.world.scr.addstr(4, 50, " "*50)
        mech.world.scr.addstr(4, 50, mech.get_specs())
        #line 4 is used for printing specs
        mech.world.scr.addstr(5, 50, " "*50)
        mech.world.scr.addstr(5, 50, mech.get_scores())
        #line 5 is used for printing scores
        for tile in mech.valid_move_tiles():
            mech.world.scr.addstr(tile.row, tile.col, str(mech.world.table[tile.row][tile.col]), curses.color_pair(mech.world.MOVE_RADIUS_COLOR_PAIR_NUM))
    def list_tiles_in_range(self, start, radius):
        frontier = Queue()
        frontier.put(start)
        visited = {}
        visited[start] = True
        while not frontier.empty() :
            current = frontier.get()
            if distance_between(start, current) <= radius:
                for n in current.neighbors():
                    if n not in visited:
                        frontier.put(n)
                        visited[n] = True
        visited.pop(start)
        return visited
    def list_walkable_tiles_in_range(self, start, radius):
        frontier = Queue()
        frontier.put(start)
        visited = {}
        visited[start] = True
        steps_taken = 0
        while not frontier.empty():
            current = frontier.get()
            if self.walking_distance_between(start, current) <= radius:
                for next in self.walkable_neighbors(current):
                    if next not in visited:
                        frontier.put(next)
                        visited[next] = True
                        steps_taken += 1
                steps_taken -= 1

        visited.pop(start)
        return visited
    def walking_distance_between(self,t1,t2):
        frontier = Queue()
        frontier.put(t1)
        came_from = {}
        came_from[t1] = None
        while not frontier.empty():
           current = frontier.get()
           if current == t2:
               break
           for n in self.walkable_neighbors(current):
              if n not in came_from:
                 frontier.put(n)
                 came_from[n] = current
        current = t2
        path = []
        while current != t1:
            path.append(current)
            current = came_from[current]
        return len(path)
    def walkable_neighbors(self, tile):
        neighbors = []
        if tile.row - 1 > 0 and self.is_walkable(location(tile.row - 1 , tile.col)):
            neighbors.append(location(tile.row-1,tile.col))
        if tile.row + 1 < Dimesions.TABLE_HEIGHT and self.is_walkable(location(tile.row + 1, tile.col)):
            # print(self.table[tile.row][tile.col])
            # print(tile.row + 1, tile.col)
            # pass
            neighbors.append(location(tile.row + 1, tile.col))
        if tile.col - 1 > 0 and self.is_walkable(location(tile.row, tile.col - 1)):
            neighbors.append(location(tile.row, tile.col - 1))
        if tile.col + 1 < Dimesions.TABLE_WIDTH and self.is_walkable(location(tile.row, tile.col + 1)):
            neighbors.append(location(tile.row, tile.col + 1))
        return neighbors
    def is_walkable(self, tile):
        return not (isinstance(self.table[tile.row][tile.col], Cover) or isinstance(self.table[tile.row][tile.col], Mech))
    def display_table(self):
        for r in range(len(self.table)):
            for c in range(len(self.table[r])):
                if r == 0:
                    col_title = ""
                    if c <= 25:
                        col_title = chr(c + 97)
                    else:
                        col_title = chr(c + 39)
                    print(col_title + " " , end = "")
                else:
                    print(str(self.table[r][c]) + " ", end = "")
            if r == 0:
                print()
            else:
                print(r)
    def curses_display_table(self):
        # print(">")
        for r in range(len(self.table)):
            for c in range(len(self.table[r])):
                if r == 0:
                    col_title = ""
                    if c <= 25:
                        col_title = chr(c + 97)
                    else:
                        col_title = chr(c + 39)
                    self.scr.addstr(r,c, col_title)
                else:
                    if isinstance(self.table[r][c], Cover):
                        self.scr.addstr(r,c,str(self.table[r][c].height), curses.color_pair(self.COVER_COLOR_PAIR_NUM))
                    else:
                        if isinstance(self.table[r][c], Mech):
                            m = self.table[r][c]
                            self.scr.addstr(str(m), curses.color_pair(m.team.num))
                            # self.window.addstr(r,c, str(m), curses.color_pair(self.color_pairs[m.team.num]))
                        else:
                            self.scr.addstr(r,c,self.table[r][c].__str__())
                    # print(str(self.table[r][c]) + " ", end = "")
            if r == 0:
                # self.window.addstr(r,c,"")
                pass
            else:
                self.scr.addstr(r,c,str(r))

    def add_team(self, team):
        team.set_num(len(self.teams)+1)
        # self.window.move(0, 0)
        curses.init_pair(team.num, team.num, curses.COLOR_BLACK)
        # self.window.scr.addstr("setting color" + str(team.num), curses.color_pair(team.num))
        self.teams.append(team)
    def has_winner(self):
        return len(self.get_active_teams()) == 1
    def get_winner(self):
        return self.get_active_teams()[0]
    def get_active_teams(self):
        active_teams = []
        for team in self.teams:
            if len(team.get_active_mechs()) > 0:
                active_teams.append(team)
        return active_teams
    def get_all_active_mechs(self):
        active_mechs = []
        for team in self.teams:
            for mech in team.mechs:
                if mech.is_active():
                    active_mechs.append(mech)
        return active_mechs
    def get_all_mechs(self):
        mechs = []
        for team in self.teams:
            for mech in team.mechs:
                mechs.append(mech)
        return mechs
    def is_valid_turn(self, turn):
        # print(".")
        if turn is None:
            return False
        if turn.verb == "pass":
            return True
        mech = self.at(turn.get_subj_loc())
        if not isinstance(mech, Mech):
            self.scr.addstr(3, 50, " "*50)
            self.scr.addstr(3, 50, "invalid command")
            return False
        if not turn.owner == mech.team:
            self.scr.addstr(3, 50, " "*50)
            self.scr.addstr(3, 50, "not your mech")
            return False
        if not mech.is_active():
            self.scr.addstr(3, 50, " "*50)
            self.scr.addstr(3, 50, "that mech is destroyed")
            return False
        else:
            if turn.verb == "inf":
                return True
            if turn.verb == "mov":
                return mech.can_move_to(turn.get_target_loc())
            if turn.verb == "atk":
                return mech.can_attack(turn.get_target_loc())

    verbs = {"mov":Mech.move, "atk":Mech.attack, "spt":Mech.spot, "none":none, "inf":info, "pass":Team.end_turn}
