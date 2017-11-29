from Player import Player
from Turn import Turn
import random
import time
class Stupid_AI(Player):
    def get_turn(self):
        time.sleep(1)
        if not self.team.attacked_yet:
            return self.get_atk_cmd()
        else:
            if not self.team.moved_yet:
                return self.get_move_cmd()
    def get_atk_cmd(self):
        m = random.choice(self.team.mechs)
        if len(m.nearby_enemies()) > 0:
            target = random.choice(m.nearby_enemies())
            return Turn(str(m.location) + " atk " + str(target.location), self.team)
        else:
            if not self.team.moved_yet():
                return self.get_move_cmd()
            else:
                return Turn("pass", self.team)
    def get_move_cmd(self):
        return Turn("pass", self.team)
        # m = random.choice(self.team.mechs)
        # target = random.choice(m.valid_move_tiles())
        # return Turn(str(m.location) + " mov " + str(target), self.team)
