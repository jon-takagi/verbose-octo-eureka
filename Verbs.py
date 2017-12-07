from Mech import Mech
from World import World
from Team import Team
verbs = {"mov":Mech.move, "atk":Mech.attack, "spt":Mech.spot, "inf":World.info, "pass":Team.end_turn, "help":World.list_commands, "atkrng":World.show_attack_range}
