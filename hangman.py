import tkinter as tk
import random

# Hangman ASCII (replace with images if you want later)
HANGMANPICS = [
    "   +---+\n       |\n       |\n       |\n      ===",
    "   +---+\n   O   |\n       |\n       |\n      ===",
    "   +---+\n   O   |\n   |   |\n       |\n      ===",
    "   +---+\n   O   |\n  /|   |\n       |\n      ===",
    "   +---+\n   O   |\n  /|\\  |\n       |\n      ===",
    "   +---+\n   O   |\n  /|\\  |\n  /    |\n      ===",
    "   +---+\n   O   |\n  /|\\  |\n  / \\  |\n      ==="
]

WORDS = ['apple', 'banana', 'mango', 'strawberry', 'orange',
         'grape', 'pineapple', 'apricot', 'lemon', 'coconut',
         'watermelon', 'cherry', 'papaya', 'berry', 'peach',
         'lychee', 'muskmelon']

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word = random.choice(WORDS)
        self.guessed = ["_"] * len(self.word)
        self.used = []
        self.wrong = 0
        self.max_wrong = len(HANGMANPICS) - 1

        # UI setup
        self.hangman_label = tk.Label(root, text=HANGMANPICS[0], font=("Courier", 16), justify="left")
        self.hangman_label.pack(pady=10)

        self.word_label = tk.Label(root, text=" ".join(self.guessed), font=("Helvetica", 20))
        self.word_label.pack(pady=10)

        self.info_label = tk.Label(root, text="Guess the fruit name!", font=("Helvetica", 14))
        self.info_label.pack(pady=5)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        # Create letter buttons
        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            btn = tk.Button(self.buttons_frame, text=letter, width=4, height=2,
                            command=lambda l=letter.lower(): self.guess_letter(l))
            btn.grid(row=i//9, column=i%9, padx=2, pady=2)

        # Control buttons frame
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)

        self.restart_button = tk.Button(self.control_frame, text="Restart Game", command=self.restart, state="disabled")
        self.restart_button.grid(row=0, column=0, padx=10)

        self.exit_button = tk.Button(self.control_frame, text="Exit Game", command=root.destroy)
        self.exit_button.grid(row=0, column=1, padx=10)

    def guess_letter(self, letter):
        if letter in self.used:
            self.info_label.config(text=f"You already guessed '{letter.upper()}'")
            return
        self.used.append(letter)

        if letter in self.word:
            for i, ch in enumerate(self.word):
                if ch == letter:
                    self.guessed[i] = letter
            self.word_label.config(text=" ".join(self.guessed))
            self.info_label.config(text="Good guess!")
        else:
            self.wrong += 1
            self.hangman_label.config(text=HANGMANPICS[self.wrong])
            self.info_label.config(text=f"Wrong guess! ({self.wrong}/{self.max_wrong})")

        # Check win/lose
        if "_" not in self.guessed:
            self.info_label.config(text="🎉 You won! The word was " + self.word)
            self.end_game()
        elif self.wrong == self.max_wrong:
            self.info_label.config(text="😢 You lost! The word was " + self.word)
            self.end_game()

    def end_game(self):
        # Disable all letter buttons
        for child in self.buttons_frame.winfo_children():
            child.config(state="disabled")
        self.restart_button.config(state="normal")

    def restart(self):
        # Reset game state
        self.word = random.choice(WORDS)
        self.guessed = ["_"] * len(self.word)
        self.used = []
        self.wrong = 0
        self.hangman_label.config(text=HANGMANPICS[0])
        self.word_label.config(text=" ".join(self.guessed))
        self.info_label.config(text="Guess the fruit name!")
        for child in self.buttons_frame.winfo_children():
            child.config(state="normal")
        self.restart_button.config(state="disabled")


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
