from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Canvas, Color, Rectangle

from action_map import ActionMap
from camera import Camera
from graphics import Graphics

# The over-arching game combines the everything together - should be self-explanatory.
# TODO: May need to break down into screens in the future.
class ActionGame(Widget):
    action_map = ActionMap()
    graphics = Graphics()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera = Camera(self.graphics, self.action_map)
        self.add_widget(self.camera)
        self.bind(size=self.resize) # Must handle resize for children.

    def update(self, dt):
        self.camera.update()

    def on_touch_move(self, touch):
        self.camera.change_pos_by(-touch.dx, -touch.dy)

    # Resize all the children as Kivy doesn't do this by default.
    def resize(self, instance, value):
        self.camera.resize(self)

# The main application - simply create the game and schedule updates.
class ActionApp(App):
    def build(self):
        game = ActionGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    ActionApp().run()
