class ActionMap():
    tiles = []
    MAP_WIDTH_IN_TILES = 1000
    MAP_HEIGHT_IN_TILES = 1000
    T_EMPTY = 69
    T_LAND_BL = 0
    T_LAND_BR = 4
    T_LAND_TL = 84
    T_LAND_TR = 88
    T_LAND_B = 1
    T_LAND_B_DROP = 6
    T_LAND_T = 85
    T_LAND_L = 63
    T_LAND_R = 67
    T_LAND_MID = 44

    def __init__(self):
        for x in range(0, self.MAP_WIDTH_IN_TILES):
            self.tiles.append([])
            for y in range(0, self.MAP_HEIGHT_IN_TILES):
                self.tiles[x].append(self.T_EMPTY)
        self.create_island(10, 10, 30, 30)
        self.create_island(100, 100, 60, 60)

    def get_tile(self, x, y):
        if x < 0 or y < 0 or x > self.MAP_WIDTH_IN_TILES or y > self.MAP_HEIGHT_IN_TILES:
            return self.T_EMPTY
        return self.tiles[x][y]

    def width(self):
        return self.MAP_WIDTH_IN_TILES

    def height(self):
        return self.MAP_HEIGHT_IN_TILES

    def create_island(self, x, y, width, height):
        if x <= 0 or y <= 0 or x + width > self.MAP_WIDTH_IN_TILES  \
                or y + height > self.MAP_HEIGHT_IN_TILES:
            print("Out of bounds for creating island")
            return
        self.tiles[x][y] = self.T_LAND_BL
        self.tiles[x + width][y] = self.T_LAND_BR
        self.tiles[x][y + height] = self.T_LAND_TL
        self.tiles[x + width][y + height] = self.T_LAND_TR
        self.tiles[x][y - 1] = self.T_LAND_B_DROP
        self.tiles[x + width][y - 1] = self.T_LAND_B_DROP

        for i in range(1, width):
            self.tiles[x + i][y] = self.T_LAND_B
            self.tiles[x + i][y + height] = self.T_LAND_T
            self.tiles[x + i][y - 1] = self.T_LAND_B_DROP

        for j in range(1, height):
            self.tiles[x][y + j] = self.T_LAND_L
            self.tiles[x + width][y + j] = self.T_LAND_R

        for i in range(1, width):
            for j in range(1, height):
                self.tiles[x + i][y + j] = self.T_LAND_MID
