from buildings.building import Bui1ding

class Park(Bui1ding):
    dimensions = (3, 3)
    def __init__(self, spaces, upperLeftCorner, lowerRightCorner):
        super().__init__(upperLeftCorner, lowerRightCorner)
        self.buildType = "Park"
        self.description = "An open field that used to be a park."
        self.floorAmountRange = (1, 1)
        self.floorSizeRange = (8100, 8100)
        self.place(spaces)
        self.finalize()