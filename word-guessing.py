import tkinter as tk
import random
from tkinter import messagebox

# word list
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
guesses = ""
turns = 12

def update_display():
    display_word = ""
    failed = 0
    for char in word:
        if char in guesses:
            display_word += char + " "
        else:
            display_word += "_ "
            failed += 1
    word_label.config(text=display_word.strip())
    chances_label.config(text=f"Chances left: {turns}")
    if failed == 0:
        messagebox.showinfo("You Win!", f"The word was: {word}")
        root.destroy()

def guess_letter():
    global guesses, turns
    guess = entry.get().lower()
    entry.delete(0, tk.END)
    if guess and guess not in guesses:
        guesses += guess
        if guess not in word:
            turns -= 1
            if turns == 0:
                messagebox.showerror("Game Over", f"You Lose! The word was: {word}")
                root.destroy()
    update_display()

# GUI setup
root = tk.Tk()
root.title("Word Guessing Game")

word_label = tk.Label(root, text="", font=("Arial", 20))
word_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 16))
entry.pack()

submit_btn = tk.Button(root, text="Guess", command=guess_letter, font=("Arial", 14))
submit_btn.pack(pady=10)

chances_label = tk.Label(root, text=f"Chances left: {turns}", font=("Arial", 14))
chances_label.pack()

update_display()
root.mainloop()
