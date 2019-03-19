from kivy.uix.screenmanager import Screen
from subwindows.mapSubWindow import MapSubwindow
from kivy.uix.floatlayout import FloatLayout
import globals as glob
from game import Game

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.c = FloatLayout()
        self.add_widget(self.c)
        self.game = Game("test", mapSize=(50, 50))
        glob.currentGame = self.game
        #win = SubWindow(bColor=(.5, .5, .5, 1), size=(100, 300), pos=(300, 300))

    def spawnMap(self, displacement, scale):
        win = MapSubwindow(bColor=(.7, .7, .7, 1), size=(300, 300), pos=(300, 300))
        win.map.displacement = displacement
        win.map.scale = scale
        self.c.add_widget(win)
        print("spawned")

    def save(self):
        glob.currentGame.save()
