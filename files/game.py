import os
import pickle
from map_assets.map import Map
from date import Date

class Game:
    def __init__(self, file, **kwargs):
        self.file = file
        if os.path.isdir(self.file):
            with open(self.file + "/map.save", "rb") as f:
                self.map = pickle.loads(f.read())
            with open(self.file + "/time.save", "rb") as f:
                self.time = pickle.loads(f.read())
        else:
            self.map = Map(kwargs["mapSize"][0], kwargs["mapSize"][1])
            self.time = Date(0, 0, 0, 0, 0)

    def save(self):
        if not os.path.isdir(self.file):
            os.mkdir(self.file)
        with open(self.file + "/map.save", "wb") as f:
            data = pickle.dumps(self.map, protocol=pickle.HIGHEST_PROTOCOL)
            f.write(data)
        with open(self.file + "/time.save", "wb") as f:
            data = pickle.dumps(self.time, protocol=pickle.HIGHEST_PROTOCOL)
            f.write(data)