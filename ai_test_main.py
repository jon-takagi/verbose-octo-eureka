from Game import Game
from Player import Player
from Stupid_AI import Stupid_AI
from Hot_Seat_Player import Hot_Seat_Player
from Team import Team
import os
os.system("printf '\e[8;32;100t'")
g = Game("map1long.png")
human = Team(g.world, "Humans")
g.add_player(Hot_Seat_Player(g, human))
robots = Team(g.world, "Robots")
g.add_player(Stupid_AI(g, robots))
robots.create_mech("RRGG", "A3")
robots.create_mech("RRGG", "C5")
human.create_mech("RRBB", "v7")
human.create_mech("RRGG", "x5")
g.set_color_prefs(Game.default_prefs)
g.start()
