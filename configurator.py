file_name = input("Config File Name? ")
with open(file_name + ".mfz", "w+") as f:
    map_name = input("map name? ")
    f.write("M:" + map_name + "\n")
    num_of_players = int(input("num of players? "))
    for i in range(num_of_players):
        team_name = input('player ' + str(i + 1) + " team name? ")
        host = input("player " + str(i + 1) + " host name? ")
        port = input("player " + str(i+1) + " port number? ")
        f.write("t-" + team_name + "@" + host + ":" + port + "\n")
        num_of_mechs = int(input("number of mechs on " + team_name))
        for i in range(num_of_mechs):
            mech_loadout = input("mech loadout? ")
            mech_loc = input("mech location?")
            f.write("m:" + mech_loadout + "@" + mech_loc + "\n")
