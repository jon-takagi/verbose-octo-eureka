import random
class World():
    def __init__(self):
        self.table = [[0 for i in range(48)] for j in range(32)]
        for i in range(150):
            x = random.randint(0,47)
            y = random.randint(0,31)
            self.table[x][y] = random.randint(10,100)
    def get_world_state(self):
        
