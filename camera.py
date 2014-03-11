from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

# A camera class that maintains rectangles that represent tiles of a map.
# It grabs the textures from the graphics based on the index provided by
# the action map. It allows positioning of the camera anywhere on the map.
class Camera(Widget):
    tiles = [] # Tiles is a list of lists of rectangles. Reference a tile with tiles[x][y].
    CAMERA_WIDTH_IN_TILES = 35
    CAMERA_HEIGHT_IN_TILES = 20

    def __init__(self, graphics, action_map, **kwargs):
        super().__init__(**kwargs)
        self.tile_width = 8
        self.tile_height = 8
        self.graphics = graphics
        self.action_map = action_map
        self.x = 0
        self.y = 0

        self.set_up_background()
        self.set_up_tiles()

    def set_up_background(self):
        self.canvas.add(Color(0.13, 0.12, 0.15)) # Background color.
        self.background = Rectangle()
        self.background.pos = (0, 0)
        self.canvas.add(self.background)
        self.canvas.add(Color(1, 1, 1)) # Reset for textures.

    def set_up_tiles(self):
        for x in range(0, self.CAMERA_WIDTH_IN_TILES):
            self.tiles.append([])
            for y in range(0, self.CAMERA_HEIGHT_IN_TILES):
                rect = Rectangle()         # The rest of the details will be set on update.
                self.tiles[x].append(rect) # Add to the list to edit later.
                self.canvas.add(rect)      # Add to canvas for drawing.

    def update(self):
        # Offset each rectangle by how far the camera is off the grid.
        self.update_tiles(self.x % self.tile_width, self.y % self.tile_height)

    def change_pos_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def resize(self, root):
        # We need to save one extra tile for scrolling purposes. If the camera is half
        # way on a tile it will require one extra to cover them all.
        self.tile_width = root.width / (self.CAMERA_WIDTH_IN_TILES - 1)
        self.tile_height = root.height / (self.CAMERA_HEIGHT_IN_TILES - 1)
        self.pos = (0, 0)
        self.size = root.size
        self.background.size = root.size

    def update_tiles(self, offset_x, offset_y):
        for x in range(0, self.CAMERA_WIDTH_IN_TILES):
            for y in range(0, self.CAMERA_HEIGHT_IN_TILES):
                rect = self.tiles[x][y]
                # Offsets are used for camera not matching the grid perfectly.
                rect.pos = (x * self.tile_width - offset_x, y * self.tile_height - offset_y)
                rect.size = (self.tile_width, self.tile_height)
                rect.texture = self.graphics.get_map_texture( \
                        self.action_map.get_tile(self.get_tile_x(x), self.get_tile_y(y)))

    def get_tile_x(self, x):
        # (Camera left side tile x value) + (tile x value from camera left)
        return int(self.x // self.tile_width + x)

    def get_tile_y(self, y):
        # (Camera bottom tile y value) + (tile y value from camera bottom)
        return int(self.y // self.tile_height + y)
