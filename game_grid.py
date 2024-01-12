from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class GameGrid(GridLayout):
    red_btn = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 3
        self.rows = 2