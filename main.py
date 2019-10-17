from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class MainWindow(BoxLayout):
    pass


class SideBar(BoxLayout):
    select_image_button = ObjectProperty(None)

    def select_image(self):
        print("Select Image")


class TopBar(BoxLayout):
    pass


class EditorFrame(BoxLayout):
    pass


class AnnotationApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    AnnotationApp().run()
