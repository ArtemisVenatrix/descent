from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from gameScreen import GameScreen
from mapTestScreen import MapTestScreen
from kivy.config import Config

class GameApp(App):
    def build(self):
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
        return Root()

class Root(ScreenManager):
    def __init__(self):
        super().__init__()
        gameScreen = GameScreen(name="gameScreen")
        mapTestScreen = MapTestScreen(name="MapTestScreen")
        self.add_widget(gameScreen)
        self.add_widget(mapTestScreen)
        self.selected = "MapTestScreen"

myApp = GameApp()
myApp.run()