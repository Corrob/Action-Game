from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

class Camera(Widget):
    tiles = []
    CAMERA_WIDTH_IN_TILES = 28
    CAMERA_HEIGHT_IN_TILES = 21

    def __init__(self, graphics, **kwargs):
        super().__init__(**kwargs)
        self.tile_width = 8
        self.tile_height = 8
        self.graphics = graphics

        for x in range(0, self.CAMERA_WIDTH_IN_TILES):
            self.tiles.append([])
            for y in range(0, self.CAMERA_HEIGHT_IN_TILES):
                r = Rectangle()
                r.pos = (x*self.tile_width, y*self.tile_height)
                r.size = (self.tile_width, self.tile_height)
                r.texture = self.graphics.get_map_texture(0)
                self.tiles[x].append(r)
                self.canvas.add(r)

    def update(self):
        pass

    def resize(self, root):
        self.tile_width = root.width / self.CAMERA_WIDTH_IN_TILES
        self.tile_height = root.height / self.CAMERA_HEIGHT_IN_TILES
        print("Width: {width}; Height: {height}".format \
                (width=self.tile_width,height=self.tile_height))
        self.pos = (0, 0)
        self.size = (root.width, root.height)
        self.update_tiles()

    def update_tiles(self):
        for x in range(0, self.CAMERA_WIDTH_IN_TILES):
            for y in range(0, self.CAMERA_HEIGHT_IN_TILES):
                r = self.tiles[x][y]
                r.pos = (x*self.tile_width, y*self.tile_height)
                r.size = (self.tile_width, self.tile_height)
