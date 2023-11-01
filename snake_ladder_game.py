import random
from tkinter import *
from cell import Cell
from board import GameBoard

class SnakeLadderGame:
    def __init__(self, width, height, size):
        self.root = Tk()
        self.root.title("Snake and Ladder Game")
        self.board = GameBoard(width, height, size)
        self.canvas = Canvas(self.root, width=width * size, height=height * size)
        self.canvas.pack()
        self.dice_roll = 0
        self.player_position = [0, 0]
        self.roll_button = Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

    def roll_dice(self):
        self.dice_roll = random.randint(1, 6)
        self.player_position[0] += self.dice_roll
        self.player_position[1] += self.dice_roll
        self.update_ui()
        self.root.after(1000, self.roll_dice)

    def update_ui(self):
        self.canvas.delete("all")
        self.board.draw(self.canvas)
        self.draw_player(self.player_position[0], "red")
        self.draw_player(self.player_position[1], "blue")

    def draw_player(self, position, color):
        x, y = position_to_coordinates(position, self.board.width)
        x1 = x * self.board.size + self.board.size // 2
        y1 = y * self.board.size + self.board.size // 2
        self.canvas.create_oval(x1 - 10, y1 - 10, x1 + 10, y1 + 10, fill=color)

def position_to_coordinates(position, board_width):
    row = (position - 1) // board_width
    col = (position - 1) % board_width
    return col, row

if __name__ == "__main__":
    game = SnakeLadderGame(10, 10, 50)
    game.root.mainloop()
