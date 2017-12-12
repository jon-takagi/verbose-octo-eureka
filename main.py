from Game import Game
from Player import Player
import os
os.system("printf '\e[8;32;100t'")
config_name = input("config file? ")
g = Game(config_name)
g.start()
