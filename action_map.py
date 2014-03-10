class ActionMap():
    tiles = []
    MAP_WIDTH_IN_TILES = 28
    MAP_HEIGHT_IN_TILES = 21

    def __init__(self):
        pass

    def get_index(self, x, y):
        if x == 0 and y == 0:
            return 0
        elif x == 0 and y == self.MAP_HEIGHT_IN_TILES - 1:
            return 84
        elif x == self.MAP_WIDTH_IN_TILES - 1 and y == 0:
            return 4
        elif x == self.MAP_WIDTH_IN_TILES - 1 and y == self.MAP_HEIGHT_IN_TILES - 1:
            return 88
        elif x == 0:
            return 21
        elif y == 0:
            return 1
        elif x == self.MAP_WIDTH_IN_TILES - 1:
            return 67
        elif y == self.MAP_HEIGHT_IN_TILES - 1:
            return 85
        else:
            return 44
