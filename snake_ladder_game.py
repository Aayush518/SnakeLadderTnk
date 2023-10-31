# snake_ladder_game.py
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
        self.current_position = [0, 0]
        self.button = Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.button.pack()

    def roll_dice(self):
        self.dice_roll = random.randint(1, 6)
        print("Dice roll:", self.dice_roll)
        self.current_position[0] += self.dice_roll
        if self.current_position[0] > 9:
            self.current_position[0] -= 9
        self.current_position[1] += self.dice_roll
        if self.current_position[1] > 9:
            self.current_position[1] -= 9
        self.canvas.delete("all")
        self.board.draw(self.canvas)
        self.canvas.create_oval(self.current_position[0] * self.board.size + 10,
                                self.current_position[1] * self.board.size + 10,
                                self.current_position[0] * self.board.size + self.board.size - 10,
                                self.current_position[1] * self.board.size + self.board.size - 10, fill="red")
        self.root.after(1000, self.roll_dice)

if __name__ == "__main__":
    game = SnakeLadderGame(10, 10, 50)
    game.root.mainloop()
