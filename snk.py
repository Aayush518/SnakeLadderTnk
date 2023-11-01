import random
from tkinter import *

class SnakeLadderGame:
    def __init__(self, width, height, size):
        self.root = Tk()
        self.root.title("Snake and Ladder Game")
        self.canvas = Canvas(self.root, width=width * size, height=height * size)
        self.canvas.pack()
        self.players = [{"position": 1, "color": "red"}, {"position": 1, "color": "blue"}]
        self.roll_button1 = Button(self.root, text="Player Red: Roll Dice", command=lambda: self.roll_dice(0))
        self.roll_button2 = Button(self.root, text="Player Blue: Roll Dice", command=lambda: self.roll_dice(1))
        self.roll_button1.pack(side=LEFT)
        self.roll_button2.pack(side=LEFT)

        self.create_gradients()  # Create gradient colors

    def create_gradients(self):
        self.gradient_colors = {
            "red": self.create_gradient(255, 0, 0),
            "blue": self.create_gradient(0, 0, 255)
        }

    def create_gradient(self, r, g, b):
        gradient = []
        for i in range(100):
            color = f'#{int(r * (1 - i/100)):02X}{int(g * (1 - i/100)):02X}{int(b * (1 - i/100)):02X}'
            gradient.append(color)
        return gradient

    def roll_dice(self, player_index):
        dice_roll = random.randint(1, 6)
        player = self.players[player_index]
        player["position"] += dice_roll
        player["position"] = self.handle_snakes_and_ladders(player["position"])
        self.update_ui()

        if self.check_win(player["position"]):
            self.display_winner(player["color"])

    def handle_snakes_and_ladders(self, position):
        # Define your game's snakes and ladders logic here
        snakes_and_ladders = {3: 22, 17: 4, 19: 7}  # Example positions
        return snakes_and_ladders.get(position, position)

    def update_ui(self):
        self.canvas.delete("all")
        self.draw_board()
        for player in self.players:
            self.draw_player(player["position"], player["color"])

    def draw_board(self):
        for row in range(10):
            for col in range(10):
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50
                color = self.gradient_colors["blue" if (row + col) % 2 == 0 else "red"][0]  # Select the first color from the gradient list
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def draw_player(self, position, color):
        x, y = position_to_coordinates(position, 10)
        x1, y1 = x * 50, y * 50
        x2, y2 = x1 + 50, y1 + 50
        self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill=color)

    def check_win(self, position):
        # Define your winning condition here (e.g., reaching a certain position)
        return position >= 100

    def display_winner(self, color):
        self.roll_button1.config(state="disabled")
        self.roll_button2.config(state="disabled")
        Label(self.root, text=f"Player {color} wins!", font=("Helvetica", 16)).pack()

def position_to_coordinates(position, board_width):
    row = (position - 1) // board_width
    col = (position - 1) % board_width
    return col, row

if __name__ == "__main__":
    game = SnakeLadderGame(10, 10, 50)
    game.root.mainloop()
