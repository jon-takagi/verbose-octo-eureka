from Gadget import Gadget
import time
class Gadgets():
    def __init__(self, slots):
        if isinstance(slots, list):
            self.members = [slots[0], slots[1], slots[2], slots[3]]
        if isinstance(slots, str):
            self.members = []
            dice = {"atk":"R", "def":"B", "mov":"G", "spt":"Y"}
            for i in range(len(slots)):
                gadg = None
                for key in dice.keys():
                    if dice[key] == slots[i].upper():
                        gadg = Gadget(key)
                        if slots[i].lower() == slots[i]:
                            gadg.active = False
                self.members.append(gadg)
        self.update_count()

    # def __init__(self, slot1, slot2, slot3, slot4):
    def __eq__(self, other):
        if isinstance(self, Gadgets) and isinstance(other, Gadgets):
            return self.count == other.count
    def __str__(self):
        return str(self.members)
    def has_active(self):
        for m in self.members:
            if m.is_active():
                return True
        return False
    def copy(self):
        return Gadgets(self.members[0], self.members[1], self.members[2], self.members[3])
    def as_string_arr(self):
        strings = []
        for gadget in self.members:
            strings.append(str(gadget))
        return strings
    def update_count(self):
        self.count = {"atk":0, "def":0,"mov":0,"spt":0}
        for member in self.members:
            # print(self.members)
            if member.is_active():
                self.count[member.kind] += 1
