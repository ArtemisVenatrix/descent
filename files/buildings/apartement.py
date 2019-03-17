from buildings.building import Bui1ding

class Apartment(Bui1ding):
    dimensions = (2, 2)
    def __init__(self, spaces, upperLeftCorner, lowerRightCorner):
        super().__init__(upperLeftCorner, lowerRightCorner)
        self.buildType = "Apartment"
        self.description = "Apartment Complex."
        self.floorAmountRange = (3, 6)
        self.floorSizeRange = (2800, 3600)
        self.place(spaces)
        self.finalize()