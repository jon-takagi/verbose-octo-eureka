from tile_content import tile_content
class Cover(tile_content):
    def __init__(self, world, height):
        super().__init__(world)
        self.height = height
    def take_damage(damage):
        self.height -= damage
    def __str__(self):
        if self.height > 3:
            return str(self.height)
        else:
            return super().__str__()
