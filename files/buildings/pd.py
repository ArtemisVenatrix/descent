from buildings.building import Bui1ding

class PoliceDepartment(Bui1ding):
    dimensions = (1, 2)
    def __init__(self, spaces, upperLeftCorner, lowerRightCorner):
        super().__init__(upperLeftCorner, lowerRightCorner)
        self.buildType = "A police department"
        self.description = "An abandoned police department."
        self.floorAmountRange = (1, 1)
        self.floorSizeRange = (1500, 1800)
        self.place(spaces)
        self.finalize()