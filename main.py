from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Canvas, Color, Rectangle

from action_map import ActionMap
from camera import Camera
from graphics import Graphics

class ActionGame(Widget):
    action_map = ActionMap()
    graphics = Graphics()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera = Camera(self.graphics, self.action_map)
        self.add_widget(self.camera)
        self.bind(size=self.resize)

    def update(self, dt):
        self.camera.update()

    def on_touch_down(self, touch):
        self.last_touch_x = touch.x
        self.last_touch_y = touch.y

    def on_touch_move(self, touch):
        self.camera.change_pos_by(self.last_touch_x - touch.x, self.last_touch_y - touch.y )
        self.last_touch_x = touch.x
        self.last_touch_y = touch.y

    def resize(self, instance, value):
        self.camera.resize(self)

class ActionApp(App):
    def build(self):
        game = ActionGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    ActionApp().run()
