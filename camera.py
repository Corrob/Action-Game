from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

class Camera(Widget):
    tiles = []
    CAMERA_WIDTH_IN_TILES = 29
    CAMERA_HEIGHT_IN_TILES = 22

    def __init__(self, graphics, action_map, **kwargs):
        super().__init__(**kwargs)
        self.tile_width = 8
        self.tile_height = 8
        self.graphics = graphics
        self.action_map = action_map
        self.x = 0
        self.y = 0

        # Add background color
        self.canvas.add(Color(0.13, 0.12, 0.15))
        self.background = Rectangle()
        self.background.pos = (0, 0)
        self.background.size = (100, 100)
        self.canvas.add(self.background)
        self.canvas.add(Color(1, 1, 1)) # Reset for textures

        for x in range(0, self.CAMERA_WIDTH_IN_TILES):
            self.tiles.append([])
            for y in range(0, self.CAMERA_HEIGHT_IN_TILES):
                r = Rectangle()
                r.pos = (x*self.tile_width, y*self.tile_height)
                r.size = (self.tile_width, self.tile_height)
                r.texture = self.graphics.get_map_texture(self.action_map.get_tile(x, y))
                self.tiles[x].append(r)
                self.canvas.add(r)

    def update(self):
        self.update_tiles(self.x % self.tile_width, self.y % self.tile_height)

    def change_pos_by(self, dx, dy):
        self.x += dx
        self.y += dy
        if self.y < 0:
            self.y = 0
        if self.x < 0:
            self.x = 0
        if self.x > self.action_map.width() * self.tile_width:
            self.x = self.action_map.width() * self.tile_width
        if self.y > self.action_map.height() * self.tile_height:
            self.y = self.action_map.height() * self.tile_height

    def resize(self, root):
        self.tile_width = root.width / (self.CAMERA_WIDTH_IN_TILES - 1)
        self.tile_height = root.height / (self.CAMERA_HEIGHT_IN_TILES - 1)
        print("Width: {width}; Height: {height}".format \
                (width=self.tile_width,height=self.tile_height))
        self.pos = (0, 0)
        self.size = (root.width, root.height)
        self.background.size = self.size

    def update_tiles(self, offset_x = 0, offset_y = 0):
        for x in range(0, self.CAMERA_WIDTH_IN_TILES):
            for y in range(0, self.CAMERA_HEIGHT_IN_TILES):
                r = self.tiles[x][y]
                r.pos = (x*self.tile_width - offset_x, y*self.tile_height - offset_y)
                r.size = (self.tile_width, self.tile_height)
                r.texture = self.graphics.get_map_texture( \
                        self.action_map.get_tile(self.get_tile_x(x), self.get_tile_y(y)))

    def get_tile_x(self, x):
        return int(self.x // self.tile_width + x)

    def get_tile_y(self, y):
        return int(self.y // self.tile_height + y)
