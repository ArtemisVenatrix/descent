from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayoutException
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, ReferenceListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

"""class SubWindow(Widget):
    tPosRel = ListProperty()
    bcolor = ListProperty()
    posOffSet = ListProperty()
    sizeOffSet = ListProperty()

    def __init__(self, **kwargs):
        super(SubWindow, self).__init__()
        self.posOffSet = [2, 2]
        self.sizeOffSet = [2, 2]
        f = kwargs['color']
        self.size = kwargs['size']
        self.pos = kwargs['pos']
        self.size_hint = (None, None)
        self.bcolor = [f[0], f[1], f[2]]
        self.currentObj = None
        print(self.bcolor)
        self.fcolor = []
        i = 0
        for item in self.bcolor:
            print("i: " + str(i))
            if item >= 0.5:
                self.fcolor.append(item - .1)

            else:
                self.fcolor.append(item + .1)
            i += 1

        self.draw()

    def close(self, instance):
        print("Closing SubWindow...")
        self.parent.remove_widget(self)

    def draw(self, *largs):
        print("size[0]: " + str(self.size[0]))
        print("size[1]: " + str(self.size[1]))
        print("pos[0]: " + str(self.pos[0]))
        print("pos[1]: " + str(self.pos[1]))
        print(self)
        print('Drawing...')
        if len(self.children) > 0:
            for child in self.children:
                self.remove_widget(child)

        x = Button(text="X", size_hint=(None, None), pos=(self.pos[0] + self.size[0] - 21, self.pos[1] + self.size[1] - 21), size=(21, 21))
        x.bind(on_release=self.close)
        self.c = BoxLayout(pos=(self.pos[0] + 1, self.pos[1] + 1), size=(self.size[0]-2, self.size[1]-22), orientation="vertical")

        self.canvas.clear()
        with self.canvas:
            Color(self.bcolor[0], self.bcolor[1], self.bcolor[2], 1)
            Rectangle(pos=self.pos, size=self.size)
            Color(self.fcolor[0], self.fcolor[1], self.fcolor[2], 1)
            Rectangle(pos=(self.pos[0] + 1, self.pos[1] + 1), size=(self.size[0]-2, self.size[1]-22))
        self.add_widget(x)
        self.add_widget(self.c)
        if self.currentObj != None:
            self.c.clear_widgets()
            self.c.add_widget(self.currentObj)
            #self.parse(self.currentObj)

    def parse(self, obj):
        print(obj)
        self.currentObj = obj
        self.c.clear_widgets()
        for val in obj.attr:
            print(obj.attr[val])
            lbl = Label(text=(val + ": " + obj.attr[val]))
            self.c.add_widget(lbl)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return super(SubWindow, self).on_touch_down(touch)

        #print(self.size)
        #print("Mouse X: " + str(touch.x))
        #print("Mouse Y: " + str(touch.y))

        if touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[0] - 21 and touch.y > self.pos[1] + self.size[1] - 5 and touch.y < self.pos[1] + self.size[1] + 5:
            self.side = 'up'
            print("up hit detect...")
            self.yInit = self.pos[1]
            self.hInit = self.size[1]
            #self.tPosRel = touch - self.pos
            touch.grab(self)
            return True

        if touch.x > self.pos[0] + self.size[0] - 5 and touch.x < self.pos[0] + self.size[0] + 5 and touch.y > self.pos[1] + 5 and touch.y < self.pos[1] + self.size[1] - 21:
            self.side = 'right'
            print("right hit detect...")
            self.xInit = self.pos[0]
            self.wInit = self.size[0]
            touch.grab(self)
            return True

        if touch.x > self.pos[0] + 5 and touch.x < self.pos[0] + self.size[0] - 5 and touch.y > self.pos[1] - 5 and touch.y < self.pos[1] + 5:
            self.side = 'down'
            print("down hit detect...")
            self.yInit = self.pos[1]
            self.hInit = self.size[1]
            touch.grab(self)
            return True

        if touch.x > self.pos[0] - 5 and touch.x < self.pos[0] + 5 and touch.y > self.pos[1] + 5 and touch.y < self.pos[1] + self.size[1]:
            self.side = 'left'
            print("left hit detect...")
            print(self.size)
            self.xInit = self.pos[0]
            self.wInit = self.size[0]
            touch.grab(self)
            return True

        if touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[1] - 21 and touch.y > self.pos[1] + self.size[1] - 22 and touch.y < self.pos[1] + self.size[1] - 5:
            self.side = 'window'
            self.tPosRel = (touch.x - self.pos[0], touch.y - self.pos[1])
            touch.grab(self)
            return True

        if touch.x > self.pos[0] - 5 and touch.x < self.pos[0] + 5 and touch.y > self.pos[1] - 5 and touch.y < self.pos[1] + 5:
            self.side = 'leftcorner'
            print("left hit detect...")
            print(self.size)
            self.xInit = self.pos[0]
            self.wInit = self.size[0]
            self.yInit = self.pos[1]
            self.hInit = self.size[1]
            touch.grab(self)
            return True

        if touch.x > self.pos[0] + self.size[0] - 5 and touch.x < self.pos[0] + self.size[0] + 5 and touch.y > self.pos[1] - 5 and touch.y < self.pos[1] + 5:
            self.side = 'rightcorner'
            print("left hit detect...")
            print(self.size)
            self.xInit = self.pos[0]
            self.wInit = self.size[0]
            self.yInit = self.pos[1]
            self.hInit = self.size[1]
            touch.grab(self)
            return True
        return super(SubWindow, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self.drag(touch)
            return True

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            return True

    def drag(self, touch):
        def up():
            if touch.y > self.yInit + 37:
                self.size[1] = touch.y - self.pos[1]

            else:
                self.size[1] = 37

            self.draw()

        def right():
            if touch.x > self.xInit + 21:
                self.size[0] = touch.x - self.pos[0]

            else:
                self.size[0] = 21

            self.draw()

        def down():
            if touch.y < self.yInit + self.hInit - 37:
                self.size[1] = self.hInit + self.yInit - touch.y
                self.pos[1] = touch.y

            else:
                self.size[1] = 37
                self.pos[1] = self.yInit + self.hInit - 37

            self.draw()

        def left():
            if touch.x < self.xInit + self.wInit - 21:
                self.size[0] = self.wInit + self.xInit - touch.x
                self.pos[0] = touch.x

            else:
                self.size[0] = 21
                self.pos[0] = self.xInit + self.wInit - 21

            self.draw()

        def window():
            print(self.tPosRel)
            self.pos = (touch.x - self.tPosRel[0], touch.y - self.tPosRel[1])
            self.draw()

        def leftcorner():
            xgood = False
            ygood = False

            if touch.x < self.xInit + self.wInit - 21:
                self.size[0] = self.wInit + self.xInit - touch.x
                self.pos[0] = touch.x
                xgood = True

            if touch.y < self.yInit + self.hInit - 37:
                self.size[1] = self.hInit + self.yInit - touch.y
                self.pos[1] = touch.y
                ygood = True

            if not xgood:
                self.size[0] = 21
                self.pos[0] = self.xInit + self.wInit - 21

            if not ygood:
                self.size[1] = 37
                self.pos[1] = self.yInit + self.hInit - 37

            self.draw()

        def rightcorner():
            xgood = False
            ygood = False

            if touch.x > self.xInit + 21:
                self.size[0] = touch.x - self.x
                xgood = True

            if touch.y < self.yInit + self.hInit - 37:
                self.size[1] = self.hInit + self.yInit - touch.y
                self.pos[1] = touch.y
                ygood = True

            if not xgood:
                self.size[0] = 21

            if not ygood:
                self.size[1] = 37
                self.pos[1] = self.yInit + self.hInit - 37

            self.draw()

        c = {'up': up, 'right': right, 'down': down, 'left': left, 'window': window, 'leftcorner': leftcorner, 'rightcorner': rightcorner}
        c[self.side]()"""


class SubWindow(Widget):
    tPosRel = ListProperty()
    bColor = ListProperty()
    innerColor = ListProperty()
    buttonPos = ListProperty()
    innerPos = ListProperty()
    innerSize = ListProperty()

    def __init__(self, **kwargs):
        self.innerPos = (self.pos[0] + 5, self.pos[1] + 40)
        self.innerSize = (90, 265)
        self.innerColor = (.2, .2, .2, 1)
        self.bColor = (0, 0, 0, 1)
        brightnessAvg = (self.bColor[0] + self.bColor[1] + self.bColor[2])/3.0
        if brightnessAvg > .5:
            self.innerColor = (kwargs["bColor"][0] - .2, kwargs["bColor"][1] - .2, kwargs["bColor"][2] - .2, 1)
        else:
            self.innerColor = (kwargs["bColor"][0] + .2, kwargs["bColor"][1] + .2, kwargs["bColor"][2] + .2, 1)
        #print(self.innerColor)
        self.buttonPos = (self.size[0] - 30, self.size[1] - 30)
        #print(self.pos)
        super().__init__(**kwargs)
        self.innerPos = (self.pos[0] + 5, self.pos[1] + 5)
        #print(self.pos)
        #print(self.bColor)
        #print(self.size)
        self.buttonPos = (self.pos[0] + self.size[0] - 25, self.pos[1] + self.size[1] - 25)

    def on_pos(self, *args):
        self.innerPos = (self.pos[0] + 5, self.pos[1] + 5)
        self.buttonPos = (self.pos[0] + self.size[0] - 25, self.pos[1] + self.size[1] - 25)
        #print(self.innerColor)

    def on_size(self, *args):
        self.innerSize = (self.size[0] - 10, self.size[1] - 45)
        self.buttonPos = (self.pos[0] + self.size[0] - 25, self.pos[1] + self.size[1] - 25)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return super(SubWindow, self).on_touch_down(touch)

        # print(self.size)
        # print("Mouse X: " + str(touch.x))
        # print("Mouse Y: " + str(touch.y))

        if touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[0] - 30 and touch.y > self.pos[1] + self.size[
            1] - 5 and touch.y < self.pos[1] + self.size[1] + 5:
            self.side = 'up'
            print("up hit detect...")
            self.yInit = self.pos[1]
            self.hInit = self.size[1]
            # self.tPosRel = touch - self.pos
            touch.grab(self)
            return True

        if touch.x > self.pos[0] + self.size[0] - 5 and touch.x < self.pos[0] + self.size[0] + 5 and touch.y > self.pos[
            1] + 5 and touch.y < self.pos[1] + self.size[1] - 21:
            self.side = 'right'
            print("right hit detect...")
            self.xInit = self.pos[0]
            self.wInit = self.size[0]
            touch.grab(self)
            return True

        if touch.x > self.pos[0] + 5 and touch.x < self.pos[0] + self.size[0] - 5 and touch.y > self.pos[
            1] - 5 and touch.y < self.pos[1] + 5:
            self.side = 'down'
            print("down hit detect...")
            self.yInit = self.pos[1]
            self.hInit = self.size[1]
            touch.grab(self)
            return True

        if touch.x > self.pos[0] - 5 and touch.x < self.pos[0] + 5 and touch.y > self.pos[1] + 5 and touch.y < self.pos[
            1] + self.size[1]:
            self.side = 'left'
            print("left hit detect...")
            #print(self.size)
            self.xInit = self.pos[0]
            self.wInit = self.size[0]
            touch.grab(self)
            return True

        if touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[0] - 30 and touch.y > self.pos[1] + self.size[
            1] - 22 and touch.y < self.pos[1] + self.size[1] - 5:
            print("top hit detect...")
            self.side = 'window'
            self.tPosRel = (touch.x - self.pos[0], touch.y - self.pos[1])
            touch.grab(self)
            return True

        if touch.x > self.pos[0] - 5 and touch.x < self.pos[0] + 5 and touch.y > self.pos[1] - 5 and touch.y < self.pos[
            1] + 5:
            self.side = 'leftcorner'
            print("left hit detect...")
            #print(self.size)
            self.xInit = self.pos[0]
            self.wInit = self.size[0]
            self.yInit = self.pos[1]
            self.hInit = self.size[1]
            touch.grab(self)
            return True

        if touch.x > self.pos[0] + self.size[0] - 5 and touch.x < self.pos[0] + self.size[0] + 5 and touch.y > self.pos[
            1] - 5 and touch.y < self.pos[1] + 5:
            self.side = 'rightcorner'
            print("right hit detect...")
            #print(self.size)
            self.xInit = self.pos[0]
            self.wInit = self.size[0]
            self.yInit = self.pos[1]
            self.hInit = self.size[1]
            touch.grab(self)
            return True
        if touch.x > self.innerPos[0] and touch.x < self.innerPos[0] + self.innerSize[0] and touch.y > self.innerPos[1] and touch.y < self.innerPos[1] + self.innerSize[1]:
            return True
        return super(SubWindow, self).on_touch_down(touch)

    def scrolled(self, scrollDirection):
        pass

    def close(self, instance):
        print("Closing SubWindow...")
        self.parent.remove_widget(self)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self.drag(touch)
            return True

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            return True

    def drag(self, touch):
        def up():
            if touch.y > self.yInit + 37:
                self.size[1] = touch.y - self.pos[1]

            else:
                self.size[1] = 37

        def right():
            if touch.x > self.xInit + 21:
                self.size[0] = touch.x - self.pos[0]

            else:
                self.size[0] = 21

        def down():
            if touch.y < self.yInit + self.hInit - 37:
                self.size[1] = self.hInit + self.yInit - touch.y
                self.pos[1] = touch.y

            else:
                self.size[1] = 37
                self.pos[1] = self.yInit + self.hInit - 37

        def left():
            if touch.x < self.xInit + self.wInit - 21:
                self.size[0] = self.wInit + self.xInit - touch.x
                self.pos[0] = touch.x

            else:
                self.size[0] = 21
                self.pos[0] = self.xInit + self.wInit - 21

        def window():
            #print(self.tPosRel)
            self.pos = (touch.x - self.tPosRel[0], touch.y - self.tPosRel[1])

        def leftcorner():
            xgood = False
            ygood = False

            if touch.x < self.xInit + self.wInit - 21:
                self.size[0] = self.wInit + self.xInit - touch.x
                self.pos[0] = touch.x
                xgood = True

            if touch.y < self.yInit + self.hInit - 37:
                self.size[1] = self.hInit + self.yInit - touch.y
                self.pos[1] = touch.y
                ygood = True

            if not xgood:
                self.size[0] = 21
                self.pos[0] = self.xInit + self.wInit - 21

            if not ygood:
                self.size[1] = 37
                self.pos[1] = self.yInit + self.hInit - 37

        def rightcorner():
            xgood = False
            ygood = False

            if touch.x > self.xInit + 21:
                self.size[0] = touch.x - self.x
                xgood = True

            if touch.y < self.yInit + self.hInit - 37:
                self.size[1] = self.hInit + self.yInit - touch.y
                self.pos[1] = touch.y
                ygood = True

            if not xgood:
                self.size[0] = 21

            if not ygood:
                self.size[1] = 37
                self.pos[1] = self.yInit + self.hInit - 37

        c = {'up': up, 'right': right, 'down': down, 'left': left, 'window': window, 'leftcorner': leftcorner,
             'rightcorner': rightcorner}
        c[self.side]()