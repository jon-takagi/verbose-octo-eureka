def load_game(self, file_name):
    f = open(file_name,"r")
    current_team = None
    for line in f:
        if line[0] == "t":
            current_team = line[2:-1]
            print("creating new team: " + current_team)
        elif line[0] == "m":
            location = line.split("@")[1][:-1]
            print("creating " + current_team + " mech: " + line[2:6] + " at " + location)
