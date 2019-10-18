from random import random

from kivy.app import App
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class MainWindow(BoxLayout):
    pass


class SideBar(BoxLayout):
    select_image_button = ObjectProperty(None)

    def select_image(self):
        print("Select Image")


class TopBar(BoxLayout):
    pass


class EditorFrame(BoxLayout):
    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            touch.ud['rectangle'] = Rectangle(pos=(touch.x, touch.y))

    def on_touch_move(self, touch):
        width = touch.x - touch.ud['rectangle'].pos[0]
        height = touch.y - touch.ud['rectangle'].pos[1]
        touch.ud['rectangle'].size = (width, height)


class AnnotationApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    AnnotationApp().run()
