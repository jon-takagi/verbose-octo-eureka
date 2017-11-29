from location import location
class Turn():
    def __init__(self, command, owner):
        command = str(command)[2:-1]
        words = command.split(" ")
        # print(command)
        self.subj = location(words[0])
        self.verb = words[1]
        self.target = location(words[2])
        self.owner = owner
    def get_subj_loc(self):
        return self.subj
    def get_verb(self):
        return self.verb
    def get_target_loc(self):
        return self.target
    def is_valid(self):
        return False
