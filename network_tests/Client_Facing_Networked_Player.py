import socket
import time
import random
class Networked_Player():
    def __init__(self,host="localhost", port=42069):
        self.host = host
        self.port = port
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((self.host, self.port))
        self.ready_to_get_state = False
        self.cs = None
        serversocket.listen(5)
        while True:
            cs, addr = serversocket.accept()
            message = cs.recv(2048).decode()
            print(">" + message)
            if self.ready_to_get_state:
                print("current world_state: " + message)
                self.world_state = message
                self.ready_to_get_state = False
            elif message == "send turn":
                cmd = self.get_turn
                cmd = input(">?")
                cs.send(cmd.encode('ascii'))
                # return self.get_turn()
            elif message == "recieve world_state":
                self.ready_to_get_state = True
                print("")
            elif message == "wait":
                print("wait")
            elif message == "quit":
                cs.close()
    def get_turn(self):
        return random.randint(-10,10)


p3 = Networked_Player()
