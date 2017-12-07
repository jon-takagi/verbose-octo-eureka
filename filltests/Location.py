import math
class Location():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    def neighbors(self):
        return [Location((self.x+1)%48,self.y), Location((self.x-1)%48,self.y), Location(self.x, (self.y+1) % 32), Location(self.x, (self.y-1) % 32)]
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash(str(self))
