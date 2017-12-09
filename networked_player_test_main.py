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
g.add_player(Server_Facing_Networked_Player(g, remote, "localhost", 42069))
remote.create_mech("RRGG", "A3")
remote.create_mech("RRGG", "C5")
local.create_mech("RRBB", "v7")
local.create_mech("RRGG", "x5")
local.create_mech("RRGG", "z18")

third = Team(g.world, "Third")
g.add_player(Server_Facing_Networked_Player(g, third, "localhost", 42070))
third.create_mech("RRGG", "w20")
third.create_mech("RRGG", "A22")
third.create_mech("RRGG", "s18")
g.set_color_prefs(Game.default_prefs)
g.start()
