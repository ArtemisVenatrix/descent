from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.properties import NumericProperty

class ScrollViewTestScreen(Screen):
    textBodyHeight = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def addText(self):
        text = Label(text="The fitness gram pacer test is a multi stage aerobic excercise", size_hint_y=None, height=40)
        self.ids["textBody"].add_widget(text)
