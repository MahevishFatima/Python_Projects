import tkinter as tk
import random
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")

        self.low = None
        self.high = None
        self.number = None
        self.chances = 7
        self.guess_count = 0

        # --- UI Widgets ---
        self.label = tk.Label(root, text="Enter the bounds:", font=("Arial", 12))
        self.label.pack(pady=10)

        # Lower bound entry with placeholder
        self.lower_entry = tk.Entry(root, width=20, fg="grey")
        self.lower_entry.pack(pady=5)
        self.set_placeholder(self.lower_entry, "lower bound here")

        # Upper bound entry with placeholder
        self.upper_entry = tk.Entry(root, width=20, fg="grey")
        self.upper_entry.pack(pady=5)
        self.set_placeholder(self.upper_entry, "upper bound here")

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.guess_label = tk.Label(root, text="", font=("Arial", 12))
        self.guess_entry = tk.Entry(root, width=10)
        self.guess_button = tk.Button(root, text="Guess", command=self.make_guess)

    def set_placeholder(self, entry, text):
        """ Add placeholder text to an Entry widget """
        entry.insert(0, text)
        entry.bind("<FocusIn>", lambda e: self.clear_placeholder(entry, text))
        entry.bind("<FocusOut>", lambda e: self.restore_placeholder(entry, text))

    def clear_placeholder(self, entry, text):
        if entry.get() == text and entry.cget("fg") == "grey":
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def restore_placeholder(self, entry, text):
        if entry.get() == "":
            entry.insert(0, text)
            entry.config(fg="grey")

    def start_game(self):
        try:
            # Make sure placeholders are not used as values
            low_text = self.lower_entry.get()
            high_text = self.upper_entry.get()

            if low_text == "lower bound here" or high_text == "upper bound here":
                messagebox.showerror("Error", "Please enter valid numbers.")
                return

            self.low = int(low_text)
            self.high = int(high_text)

            if self.low >= self.high:
                messagebox.showerror("Error", "Lower bound must be less than upper bound.")
                return

            self.number = random.randint(self.low, self.high)
            self.guess_count = 0
            self.chances = 7

            self.label.config(
                text=f"Guess the number between {self.low} and {self.high}\nYou have {self.chances} chances."
            )
            self.lower_entry.pack_forget()
            self.upper_entry.pack_forget()
            self.start_button.pack_forget()

            self.guess_label.config(text="Enter your guess:")
            self.guess_label.pack(pady=10)
            self.guess_entry.pack(pady=5)
            self.guess_button.pack(pady=10)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def make_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.guess_count += 1

            if guess == self.number:
                self.end_game(f"🎉 You guessed it! The number was {self.number}.\nAttempts: {self.guess_count}")
            elif self.guess_count >= self.chances:
                self.end_game(f"😞 Out of chances! The number was {self.number}.")
            elif guess > self.number:
                self.label.config(text=f"Too high! Try again. Chances left: {self.chances - self.guess_count}")
            else:
                self.label.config(text=f"Too low! Try again. Chances left: {self.chances - self.guess_count}")

            self.guess_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

    def end_game(self, message):
        choice = messagebox.askyesno("Game Over", message + "\n\nDo you want to play again?")
        if choice:
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        # Reset UI
        self.guess_label.pack_forget()
        self.guess_entry.pack_forget()
        self.guess_button.pack_forget()

        self.label.config(text="Enter lower and upper bounds:")

        self.lower_entry.delete(0, tk.END)
        self.upper_entry.delete(0, tk.END)

        # Restore placeholders
        self.set_placeholder(self.lower_entry, "lower bound here")
        self.set_placeholder(self.upper_entry, "upper bound here")

        self.lower_entry.pack(pady=5)
        self.upper_entry.pack(pady=5)
        self.start_button.pack(pady=10)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
