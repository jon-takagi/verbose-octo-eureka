from Location import Location
class Tile():
    def __init__(self, x, y):
        self.data = "(" + str(x) + ", " + str(y) + ")"
        self.location = Location(x, y)
