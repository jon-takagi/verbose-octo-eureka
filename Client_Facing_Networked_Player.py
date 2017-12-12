from Player import Player
from Mech import Mech
from location_helpers import str_to_coords
from location_helpers import coords_to_str
from Turn import Turn
from Game import Game
import curses
import sys
import os
import re
import socket
import pickle
class Client_Facing_Networked_Player(Player):
    def __init__(self,host="localhost", port=42069, config_file="test_save.mfz"):
        os.system("printf '\e[8;32;100t'")
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((host, int(port)))
        self.ready_to_get_state = False
        self.expected_world_size = 0
        self.cs = None
        self.world = None
        self.has_game = False
        self.game = None
        serversocket.listen(5)
        while True:
            self.cs, addr = serversocket.accept()
            self.game = Game(config_file)
            # print("got connection from " + str(addr))
            self.run()

    def check_input(self):
        curses.echo()
        self.game.world.scr.move(2, 50)
        command = self.game.world.scr.getstr(2, 50, Player.MAX_COMMAND_LENGTH)
        return command.decode('ascii')
    def run(self):
        while self.cs != None:
            # print(self.ready_to_get_state)
            if self.ready_to_get_state:
                pickle_dump = b''
                while self.expected_world_size > 0:
                    message = self.cs.recv(self.expected_world_size)
                    pickle_dump += message
                    self.expected_world_size -= len(message)
                #     print("< awaiting " + str(self.expected_world_size))
                # print("< unpickling world of size " + str(len(pickle_dump)))
                # with open("pickle_out.pickle", "wb") as pickle_out:
                #     pickle_out.write(pickle_dump)
                self.world = pickle.loads(pickle_dump)
                self.world.load_scr()
                self.world.scr = curses.initscr()
                # print("unpickled")
                self.cs.send("done".encode('ascii'))
                # print("replied")
                self.ready_to_get_state = False
            else:
                message = self.cs.recv(1024)
                message = message.decode()
                # print(message)
                if message != "":
                    # print("> " + message)
                    if message == "send turn":
                        cmd = self.get_turn
                        self.world.curses_display_table()
                        # cmd = input(">?")
                        cmd = self.check_input()
                        self.cs.send(cmd.encode('ascii'))
                        # return self.get_turn()
                    elif message == "wait":
                        # print("< waiting")
                        pass
                    elif message == "quit":
                        self.cs.close()
                    else:
                        splits = message.split(":")
                        if splits[0] == "recieve world_state":
                            self.expected_world_size = int(splits[1])
                            self.cs.send("ready".encode("ascii"))
                            self.ready_to_get_state = True
                            # print("< expecting world size: " + str(self.expected_world_size))
if len(sys.argv) == 1:
    c = Client_Facing_Networked_Player()
elif len(sys.argv) == 2:
    c = Client_Facing_Networked_Player("localhost", sys.argv[1])
elif len(sys.argv) == 3:
    c = Client_Facing_Networked_Player(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 4:
    c = Client_Facing_Networked_Player(sys.argv[1], sys.argv[2], sys.argv[3])
    # print("")
