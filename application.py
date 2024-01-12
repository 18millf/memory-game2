from kivy.app import App

from main_window import MainWindow

class Application(App):
    def build(self):
        return MainWindow()