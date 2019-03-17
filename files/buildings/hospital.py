from buildings.building import Bui1ding

class Hospital(Bui1ding):
    dimensions = (2, 2)
    def __init__(self, spaces, upperLeftCorner, lowerRightCorner):
        super().__init__(upperLeftCorner, lowerRightCorner)
        self.buildType = "Hospital"
        self.description = "A hospital or something."
        self.floorAmountRange = (3, 4)
        self.floorSizeRange = (2800, 3600)
        self.place(spaces)
        self.finalize()