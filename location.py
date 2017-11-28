import math
from location_helpers import str_to_coords
from location_helpers import coords_to_str
from location_helpers import distance_between
from td import Dimesions
# from table_dimensions import TABLE_HEIGHT
class location():
    def __init__(self,a1, a2=None):
        if a2 == None:
            cords = str_to_coords(a1)
            self.row = cords[0]
            self.col = cords[1]
        else:
            self.row = a1
            self.col = a2
    def distance_to(self,other):
        return distance_between(self, other)
    def as_coords(self):
        return (self.row, self.col)
    def as_str(self):
        return str(self)
    def __str__(self):
        return (chr(self.col + 97) if self.col < 26 else chr(self.col + 39) )+ str(self.row)
    def neighbors(self):
        neighbors = []
        if self.row - 1 > 0:
            neighbors.append(location(self.row-1,self.col))
        if self.row + 1 < Dimesions.TABLE_WIDTH:
            neighbors.append(location(self.row + 1, self.col))
        if self.col - 1 > 0:
            neighbors.append(location(self.row, self.col - 1))
        if self.col + 1 < Dimesions.TABLE_HEIGHT:
            neighbors.append(location(self.row, self.col + 1))
        return neighbors
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    def __hash__(self):
        return hash(str(self))
