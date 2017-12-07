import socket
import time
import random
class Networked_Player():
    def __init__(self,host="localhost", port=42069):
        self.host = host
        self.port = port
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((self.host, self.port))
        self.cs = None
        serversocket.listen(5)
        while True:
            cs, addr = serversocket.accept()
            message = cs.recv(2048).decode()
            print(">" + message)
            if message == "send turn":
                cmd = self.get_turn
                cmd = input(">?")
                cs.send(cmd.encode('ascii'))
                # return self.get_turn()
            elif message == "wait":
                print("wait")
                pass
            elif message == "quit":
                cs.close()
    def get_turn(self):
        def coords_to_str(t):
            return (chr(t[1] + 97) if t[1] < 26 else chr(t[1] + 39) )+ str(t[0])
        x1 = random.randint(0,47)
        x2 = random.randint(0,47)
        y1 = random.randint(0,31)
        y2 = random.randint(0,31)
        p1 = coords_to_str((x1, y1))
        p2 = coords_to_str((x2, y2))
        verbs = ["mov", "atk"]
        time.sleep(1)
        cmd = p1 + " " + random.choice(verbs) + " " + p2
        return cmd


p3 = Networked_Player()
