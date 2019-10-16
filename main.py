from kivy.app import App
from kivy.uix.widget import Widget


class MainWindow(Widget):
    pass


class AnnotationApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    AnnotationApp().run()
