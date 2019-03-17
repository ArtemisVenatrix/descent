from subWindow import SubWindow
from mapScreenObject import MapScreenObject
from map import Map
import pickle
import numpy

class MapSubwindow(SubWindow):
    def __init__(self, **kwargs):
        self.ready = False
        super().__init__(**kwargs)
        map = self.loadMap()
        self.map = MapScreenObject(map)
        self.map.size = self.ids["content"].size
        self.map.pos = self.ids["content"].pos
        self.ids["content"].bind(size=self.update)
        self.ids["content"].bind(pos=self.update)
        self.ids["content"].add_widget(self.map)
        self.ready = True

    def update(self, *args):
        self.map.size = self.ids["content"].size
        self.map.pos = self.ids["content"].pos

    def close(self, instance):
        with open("data/map", 'wb') as f:
            data = pickle.dumps(self.map.map)
            f.write(data)
        print("Closing SubWindow...")
        self.parent.remove_widget(self)

    def loadMap(self):
        try:
            with open("data/map", 'rb') as f:
                if len(f.read()) > 0:
                    f.seek(0)
                    map = pickle.loads(f.read(), fix_imports=True)
                    print(map)
                else:
                    map = Map(50, 50)
            return map
        except:
            with open("data/map", 'wb') as f:
                pass
            self.loadMap()

    def scrolled(self, scrollDirection):
        if scrollDirection == 'scrollup':
            self.map.scale = float(numpy.clip(self.map.scale - 0.5, 1.0, 10.0))
        else:
            self.map.scale = float(numpy.clip(self.map.scale + 0.5, 1.0, 10.0))

    def on_touch_down(self, touch):
        if touch.x > self.ids["content"].pos[0] and touch.x < self.ids["content"].pos[0] + self.ids["content"].size[0] and touch.y > self.ids["content"].pos[1] and touch.y < self.ids["content"].pos[1] + self.ids["content"].size[1] and touch.is_mouse_scrolling:
            self.scrolled(touch.button)
        elif  touch.x > self.ids["content"].pos[0] and touch.x < self.ids["content"].pos[0] + self.ids["content"].size[0] and touch.y > self.ids["content"].pos[1] and touch.y < self.ids["content"].pos[1] + self.ids["content"].size[1]:
            self.map.isBeingMoved = True
            print("content clicked...")
        else:
            return super(MapSubwindow, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        #print(self.map.displacement)
        if self.map.isBeingMoved:
            self.map.displacement[0] += touch.dx
            self.map.displacement[1] += touch.dy
        else:
            return super(MapSubwindow, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.map.isBeingMoved:
            self.map.isBeingMoved = False
        else:
            return super(MapSubwindow, self).on_touch_up(touch)