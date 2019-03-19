from kivy.uix.floatlayout import FloatLayout

class JournalScreenObject(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.pos)