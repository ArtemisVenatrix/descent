from kivy.uix.screenmanager import Screen

class MapTestScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.add_widget(Map(10, 10))