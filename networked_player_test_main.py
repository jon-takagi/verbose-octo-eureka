from Game import Game
from Player import Player
from Server_Facing_Networked_Player import Server_Facing_Networked_Player
from Hot_Seat_Player import Hot_Seat_Player
from Team import Team
import os
os.system("printf '\e[8;32;100t'")
g = Game("map1long.png")
local = Team(g.world, "Local")
g.add_player(Hot_Seat_Player(g, local))
remote = Team(g.world, "Remote")
g.add_player(Server_Facing_Networked_Player(g, remote))
remote.create_mech("RRGG", "A3")
remote.create_mech("RRGG", "C5")
local.create_mech("RRBB", "v7")
local.create_mech("RRGG", "x5")
local.create_mech("RRGG", "z18")
g.set_color_prefs(Game.default_prefs)
g.start()
