from jsonObject import JsonObject
from floor import Floor
import random as rand

class Bui1ding:
    dimensions = (0, 0)
    def __init__(self, upperLeftCorner, lowerRightCorner):
        self.color = (0, 0, 0, 0)
        self.upperLeftCorner = upperLeftCorner
        self.lowerRightCorner = lowerRightCorner
        self.myDimensions = (lowerRightCorner[0] - upperLeftCorner[0], lowerRightCorner[1] - upperLeftCorner[1])
        self.spaces = []
        self.name = ""
        self.description = ""
        self.buildType = ""
        self.floorSizeRange = (0, 0)
        self.floorSize = 0
        self.floorAmountRange = (0, 0)
        self.floorAmount = 0
        self.floors = []
        self.owningFaction = None
        self.resources = {"constructionResources": 0, "food": 0}

    def place(self, spaces):
        self.spaces = spaces
        for x in spaces:
            if not x.occupant == None:
                raise Exception("Attempt to override occupied cell.")
            x.occupant = self

    def finalize(self):
        self.floorSize = rand.randint(self.floorSizeRange[0], self.floorSizeRange[1])
        self.floorAmount = rand.randint(self.floorAmountRange[0], self.floorAmountRange[1])
        for x in range(self.floorAmount):
            self.floors.append(Floor(self.floorSize))