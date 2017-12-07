import random
import time
from Turn import Turn
class Test_Player():
    def __init__(self, name):
        self.name = name
    def get_turn(self):
        def coords_to_str(t):
            return (chr(t[1] + 97) if t[1] < 26 else chr(t[1] + 39) )+ str(t[0])
        x1 = random.randint(0,47)
        x2 = random.randint(0,47)
        y1 = random.randint(0,31)
        y2 = random.randint(0,31)
        p1 = coords_to_str((x1, y1))
        p2 = coords_to_str((x2, y2))
        verbs = ["mov", "atk"]
        time.sleep(.5)
        cmd = p1 + " " + random.choice(verbs) + " " + p2
        return self.name + ": " + cmd
