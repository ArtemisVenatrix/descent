from buildings.building import Bui1ding

class House(Bui1ding):
    dimensions = (1, 1)
    def __init__(self, spaces, upperLeftCorner, lowerRightCorner):
        super().__init__(upperLeftCorner, lowerRightCorner)
        self.buildType = "House"
        self.description = "A house that people live in."
        self.floorAmountRange = (1, 2)
        self.floorSizeRange = (700, 900)
        self.place(spaces)
        self.finalize()