from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty
import numpy
import globals as glob

class MapScreenObject(Widget):
    scale = NumericProperty(1.0)
    displacement = ListProperty()
    def __init__(self):
        self.displacement = (0, 0)
        super().__init__()
        self.map = glob.currentGame.map
        self.isBeingMoved = False
        self.draw()

    def draw(self):
        self.canvas.clear()
        with self.canvas:
            smallestSize = min(self.size[0], self.size[1]) * self.scale
            cellSize = smallestSize/self.map.grid.width
            for x in self.map.buildings:
                pos = (self.pos[0] + cellSize*x.upperLeftCorner[0], self.pos[1] + cellSize*x.upperLeftCorner[1])
                size = (x.myDimensions[0]*cellSize, x.myDimensions[1]*cellSize)
                Color(0, 0, 0, 1)
                Line(points=[pos[0], pos[1], pos[0] + size[0], pos[1]], width=3)
                Line(points=[pos[0] + size[0], pos[1], pos[0] + size[0], pos[1] + size[1]], width=3)
                Line(points=[pos[0], pos[1] + size[1], pos[0] + size[0], pos[1] + size[1]], width=3)
                Line(points=[pos[0], pos[1], pos[0], pos[1] + size[1]], width=3)
            Color(0, 0, 0, 1)
            yPosNorm1 = self.pos[1] + (self.size[1] - smallestSize/self.scale)/2
            yPosNorm2 = self.pos[1] + smallestSize/self.scale + (self.size[1] - smallestSize/self.scale)/2
            xPosNorm1 = self.pos[0] + (self.size[0] - smallestSize/self.scale)/2
            xPosNorm2 = self.pos[0] + smallestSize/self.scale + (self.size[0] - smallestSize/self.scale)/2
            rowLineSizeDiff = ((xPosNorm2 - xPosNorm1)*self.scale - (xPosNorm2 - xPosNorm1))/2
            colLineSizeDiff = ((yPosNorm2 - yPosNorm1)*self.scale - (yPosNorm2 - yPosNorm1))/2
            for i in range(self.map.grid.height + 1):
                rowLinePos = self.pos[1] + smallestSize/self.map.grid.height * i + (self.size[1] - smallestSize)/2 + self.displacement[1]
                if rowLinePos >=  yPosNorm1 and rowLinePos <= yPosNorm2:
                    Line(points=[float(numpy.clip(xPosNorm1 + self.displacement[0] - rowLineSizeDiff, xPosNorm1, xPosNorm2)), rowLinePos, float(numpy.clip(xPosNorm2 + self.displacement[0] + rowLineSizeDiff, xPosNorm1, xPosNorm2)), rowLinePos], width=1)
            for i in range(self.map.grid.width + 1):
                colLinePos = self.pos[0] + smallestSize/self.map.grid.width * i + (self.size[0] - smallestSize)/2 + self.displacement[0]
                if colLinePos >= xPosNorm1 and colLinePos <= xPosNorm2:
                    Line(points=[colLinePos, float(numpy.clip(yPosNorm1 + self.displacement[1] - colLineSizeDiff, yPosNorm1, yPosNorm2)), colLinePos, float(numpy.clip(yPosNorm2 + self.displacement[1] + colLineSizeDiff, yPosNorm1, yPosNorm2))], width=1)

    def on_size(self, *args):
        self.draw()

    def on_pos(self, *args):
        self.draw()

    def on_scale(self, *args):
        self.draw()

    def on_displacement(self, *args):
        self.draw()