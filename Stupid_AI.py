from Player import Player
import random
class Stupid_AI(Player):
    def get_turn(self):
        if not self.team.attacked_yet:
            return self.get_atk_cmd()
        else:
            if not self.team.moved_yet:
                return self.get_move_cmd()
    def get_atk_cmd(self):
        m = random.choice(self.team.mechs)
        if len(m.nearby_enemies()) > 0:
            target = random.choice(m.nearby_enemies())
            return Turn(m.location + " atk " + target.location)
        else:
            if not self.team.moved_yet():
                return self.get_move_cmd()
            else:
                return Turn("pass", self.team)
    def get_move_cmd(self):
        m = random.choice(self.team.mechs)
        target = random.choice(m.valid_move_tiles())
        return Turn(m.location + " mov " + target)
