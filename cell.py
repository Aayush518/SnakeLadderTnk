
class Cell:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.id = str(x) + " " + str(y)
        self.color = "white"
        self.ladder = False
        self.snake = False

    def draw(self, canvas):
        x1 = self.x * self.size
        y1 = self.y * self.size
        x2 = x1 + self.size
        y2 = y1 + self.size
        canvas.create_rectangle(x1, y1, x2, y2, fill=self.color, outline="black")
        canvas.create_text(x1 + self.size // 2, y1 + self.size // 2, text=self.id)
