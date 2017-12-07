from Game import Game
from Player import Player
import os
os.system("printf '\e[8;32;100t'")
g = Game("StationMap.png")
g.load_game("test_save.mfz")
g.start()
