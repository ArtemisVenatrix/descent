from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.gameScreen import GameScreen
from screens.mapTestScreen import MapTestScreen
from screens.ScrollViewTestScreen import ScrollViewTestScreen
from kivy.config import Config
import globals as glob

class GameApp(App):
    def build(self):
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
        return Root()

class Root(ScreenManager):
    def __init__(self):
        super().__init__()
        gameScreen = GameScreen(name="gameScreen")
        glob.currentGameScreen = gameScreen
        mapTestScreen = MapTestScreen(name="MapTestScreen")
        scrollViewTestScreen = ScrollViewTestScreen(name="scrollViewTestScreen")
        self.add_widget(gameScreen)
        self.add_widget(mapTestScreen)
        self.add_widget(scrollViewTestScreen)
        self.current = "gameScreen"

myApp = GameApp()
myApp.run()