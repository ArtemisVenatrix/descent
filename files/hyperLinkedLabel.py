from kivy.uix.label import Label
import globals as glob

class HyperLinkedLabel(Label):
    def __init__(self, eventPos, **kwargs):
        super().__init__(**kwargs)
        self.eventPos = eventPos

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.openEvent()
        else:
            return super(HyperLinkedLabel, self).on_touch_down(touch)