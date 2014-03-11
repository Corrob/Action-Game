from kivy.uix.image import Image

# A graphics manager that manages loading images and provides utility
# for other classes to retrieve them.
class Graphics:
    SHEET_TILE_WIDTH = 16
    SHEET_TILE_HEIGHT = 16
    SHEET_WIDTH_IN_TILES = 21
    SHEET_HEIGHT_IN_TILES = 5

    def __init__(self):
        self.map_sheet = Image(source="dungeon.png")

    def get_map_texture(self, index):
        # Determine the x and y value of an index. X is tiles to the right and Y is
        # tiles up from the bottom. The bottom left tile is index 0 and increases to the
        # right and filling up the row and progressing upward.
        x, y = index % self.SHEET_WIDTH_IN_TILES, index // self.SHEET_WIDTH_IN_TILES
        # There were issues involved with using the entire tile. When scaled, bits
        # and pieces outside the region specified were displayed. A one pixel buffer
        # is then created around the tile.
        # TODO: Determine the root cause and see if the issue above can be resolved.
        return self.map_sheet.texture.get_region(x * self.SHEET_TILE_WIDTH + 1, \
                y * self.SHEET_TILE_HEIGHT + 1, self.SHEET_TILE_WIDTH - 2, \
                self.SHEET_TILE_HEIGHT - 2)
