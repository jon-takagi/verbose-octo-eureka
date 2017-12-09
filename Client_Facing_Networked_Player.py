from Player import Player
from Mech import Mech
from location_helpers import str_to_coords
from location_helpers import coords_to_str
from Turn import Turn
import curses
import re
import socket
import pickle
class Client_Facing_Networked_Player(Player):
    def __init__(self,host="localhost", port=42069):
        self.host = host
        self.port = port
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((self.host, self.port))
        self.ready_to_get_state = False
        self.expected_world_size = 0
        self.cs = None
        serversocket.listen(5)
        while True:
            cs, addr = serversocket.accept()
            if self.ready_to_get_state:
                pickle_dump = ""
                while self.expected_world_size > 0:
                    message = cs.recv(self.expected_world_size).decode()
                    print(message)
                    print("< recieved " + str(len(message)))
                    pickle_dump += message
                    print("< awaiting " + str(self.expected_world_size))
                    self.expected_world_size -= len(message)
                print("< unpickling world of size " + str(len(pickle_dump)))

                self.world_state = pickle.loads(pickle_dump)
                print("< current world_state: " + self.world_state)
                self.ready_to_get_state = False
            else:
                message = cs.recv(1024)
                message = message.decode()
                # print(message)
                print("> " + message)
                if message == "send turn":
                    cmd = self.get_turn
                    cmd = input(">?")
                    cs.send(cmd.encode('ascii'))
                    # return self.get_turn()
                elif message[0:19] == "recieve world_state":
                    self.expected_world_size = int(message.split(":")[1])
                    cs.send("ready".encode("ascii"))
                    self.ready_to_get_state = True
                    print("< expecting world size: " + str(self.expected_world_size))
                elif message == "wait":
                    print("< waiting")
                elif message == "quit":
                    cs.close()
c = Client_Facing_Networked_Player()
