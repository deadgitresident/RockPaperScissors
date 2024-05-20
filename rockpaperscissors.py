import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

class RockPaperScissors(tk.Tk):
    """Rock, Paper, Scissors game."""

    def __init__(self):
        super().__init__()
        self.title("Rock, Paper, Scissors")
        self.geometry("300x200")
        
        self.count_h = 0
        self.count_c = 0

        self.label_score = tk.Label(self, text=f"Human: {self.count_h} | Computer: {self.count_c}")
        self.label_score.pack(pady=10)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=10)

        self.rock_button = tk.Button(self.button_frame, text="Rock", width=10, command=lambda: self.play_game('rock'))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", width=10, command=lambda: self.play_game('paper'))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", width=10, command=lambda: self.play_game('scissors'))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.new_game_button = tk.Button(self, text="New Game", width=10, command=self.new_game)
        self.new_game_button.pack(pady=10)

    def play_game(self, user_choice):
        """Play a single game of Rock, Paper, Scissors."""
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        result = determine_winner(user_choice, computer_choice)
        messagebox.showinfo("Result", f"The computer chose {computer_choice}.\n{result}")
        if result == "You win!":
            self.count_h += 1
        elif result == "Computer wins!":
            self.count_c += 1
        self.update_scores()

    def update_scores(self):
        """Update the score labels."""
        self.label_score.config(text=f"Human: {self.count_h} | Computer: {self.count_c}")

    def new_game(self):
        """Reset the scores."""
        self.count_h = 0
        self.count_c = 0
        self.update_scores()

if __name__ == "__main__":
    app = RockPaperScissors()
    app.mainloop()