from Game import Game
from Player import Player
import os
os.system("printf '\e[8;32;100t'")
args=input("host:port?")
host, port = args.split(":")[0], args.split(":")[1]
