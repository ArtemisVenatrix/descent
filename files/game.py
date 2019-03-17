import os
import pickle
from map import Map

class Game:
    def __init__(self, file, **kwargs):
        self.file = file
        if os.path.isdir(self.file):
            with open(self.file + "/map.save", "rb") as f:
                self.map = pickle.loads(f.read())
        else:
            self.map = Map(kwargs["mapSize"][0], kwargs["mapSize"][1])

    def save(self):
        if not os.path.isdir(self.file):
            os.mkdir(self.file)
        with open(self.file + "/map.save", "wb") as f:
            data = pickle.dumps(self.map, protocol=pickle.HIGHEST_PROTOCOL)
            f.write(data)