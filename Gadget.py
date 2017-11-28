class Gadget():
    kinds = ["atk", "def", "mov", "spt"]
    def __init__(self, k):
        if k in Gadget.kinds:
            self.kind = k
        self.active = True
    def __str__(self):
        return self.kind
    def __repr__(self):
        return self.kind
    def is_active(self):
        return self.active
    def copy(self):
        return Gadget(self.kind)
