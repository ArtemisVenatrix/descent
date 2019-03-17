from buildings.building import Bui1ding

class SuperMarket(Bui1ding):
    dimensions = (2, 3)
    def __init__(self, spaces, upperLeftCorner, lowerRightCorner):
        super().__init__(upperLeftCorner, lowerRightCorner)
        self.buildType = "SuperMarket"
        self.description = "A store with commodities."
        self.floorAmountRange = (1, 1)
        self.floorSizeRange = (4500, 5400)
        self.place(spaces)
        self.finalize()