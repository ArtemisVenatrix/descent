from buildings.building import Bui1ding

class Mall(Bui1ding):
    dimensions = (3, 3)
    def __init__(self, spaces, upperLeftCorner, lowerRightCorner):
        super().__init__(upperLeftCorner, lowerRightCorner)
        self.buildType = "Mall"
        self.description = "A shopping mall."
        self.floorAmountRange = (2, 3)
        self.floorSizeRange = (7800, 8100)
        self.place(spaces)
        self.finalize()