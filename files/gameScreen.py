from kivy.uix.screenmanager import Screen
from subWindow import SubWindow
from mapSubWindow import MapSubwindow
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.c = FloatLayout()
        self.add_widget(self.c)
        #win = SubWindow(bColor=(.5, .5, .5, 1), size=(100, 300), pos=(300, 300))

    def spawnMap(self):
        win = MapSubwindow(bColor=(.7, .7, .7, 1), size=(300, 300), pos=(300, 300))
        self.c.add_widget(win)
        print("spawned")

class TestObject(Widget):
    pass
