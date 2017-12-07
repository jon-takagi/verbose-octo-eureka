from Test_Player import Test_Player
from Test_Host import Test_Host
from Networked_Player_Front import Networked_Player_Front
p1 = Test_Player("p1")
p2 = Test_Player("p2")
p3 = Networked_Player_Front("p3")
host = Test_Host()
host.add_player(p1)
host.add_player(p2)
host.add_player(p3)
host.start()
