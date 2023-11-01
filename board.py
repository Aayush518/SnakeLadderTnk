class GameBoard:
    def __init__(self, width, height, size):
        self.width = width
        self.height = height
        self.size = size
        self.grid = [[Cell(x, y, size) for x in range(width)] for y in range(height)]

    def draw(self, canvas):
        for row in self.grid:
            for cell in row:
                cell.draw(canvas)
