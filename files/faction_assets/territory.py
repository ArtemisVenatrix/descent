class Territory:
    def __init__(self):
        self.buildings = []
        self.cells = []

    def addBuilding(self, building):
        self.buildings.append(building)
        for x in building.spaces:
            self.cells.append(x)