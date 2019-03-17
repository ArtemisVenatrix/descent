from jsonObject import JsonObject
from grid import Grid


class Map:
    def __init__(self, h, w):
        self.grid = Grid(h, w)
        #buildings are stored here
        self.buildings = []