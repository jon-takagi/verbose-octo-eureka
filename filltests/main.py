from Tile import Tile
from Location import Location
from queue import Queue

def list_tiles_in_range(start, radius):
        frontier = Queue()
        frontier.put(start)
        visited = {}
        visited[start] = True
        while not frontier.empty() :
            current = frontier.get()
            for n in current.neighbors():
                if n not in visited:
                    frontier.put(n)
                    visited[n] = True
                else:
                    print(">")
        return visited

table = [[Tile(i, j) for i in range(20)] for j in range(20)]
print("table built")
for tile in list_tiles_in_range(Location(10,10), 5):
    print(tile.data)
