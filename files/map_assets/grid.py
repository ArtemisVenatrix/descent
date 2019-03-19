from map_assets.cell import Cell


class Grid:
    def __init__(self, height, width):
        self.grid = []
        self.height = height
        self.width = width
        for i in range(height):
            self.grid.append([])
            for j in range(width):
                self.grid[i].append(Cell(i, j))
