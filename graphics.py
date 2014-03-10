from kivy.uix.image import Image

class Graphics:
    SHEET_TILE_WIDTH = 16
    SHEET_TILE_HEIGHT = 16
    SHEET_WIDTH_IN_TILES = 21
    SHEET_HEIGHT_IN_TILES = 5

    def __init__(self):
        self.map_sheet = Image(source="dungeon.png")

    def get_map_texture(self, index):
        x, y = index % self.SHEET_WIDTH_IN_TILES, index // self.SHEET_WIDTH_IN_TILES
        return self.map_sheet.texture.get_region(x * self.SHEET_TILE_WIDTH + 1, \
                y * self.SHEET_TILE_HEIGHT + 1, self.SHEET_TILE_WIDTH - 2, \
                self.SHEET_TILE_HEIGHT - 2)
