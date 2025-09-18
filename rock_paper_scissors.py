import tkinter as tk
import random

# Window setup
root = tk.Tk()
root.title("Rock Paper Scissors 🤘📄✂️")
root.geometry("500x400")
root.config(bg="#1e1e2f")  # dark background

choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

# Functions
def play(user_choice):
    comp_choice = random.choice(choices)
    user_label.config(text=f"User: {user_choice} {emojis[user_choice]}", fg="#00ffcc")
    comp_label.config(text=f"Computer: {comp_choice} {emojis[comp_choice]}", fg="#ffcc00")

    if user_choice == comp_choice:
        result_label.config(text="It's a Tie! 😅", fg="lightblue")
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result_label.config(text="You Win! 🎉😂", fg="lime")
    else:
        result_label.config(text="Computer Wins! 🤖💀", fg="red")

# Title
title_label = tk.Label(root, text="🎮 Rock Paper Scissors 🎮", 
                       font=("Comic Sans MS", 20, "bold"), 
                       bg="#1e1e2f", fg="#ff99cc")
title_label.pack(pady=10)

# Frame for buttons
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=20)

# Buttons
rock_btn = tk.Button(btn_frame, text="🪨 Rock", font=("Arial", 15, "bold"),
                     bg="#ff6666", fg="white", width=10,
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="📄 Paper", font=("Arial", 15, "bold"),
                      bg="#66ccff", fg="white", width=10,
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="✂️ Scissors", font=("Arial", 15, "bold"),
                         bg="#99cc33", fg="white", width=10,
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Labels for choices and result
user_label = tk.Label(root, text="User: ", font=("Arial", 14, "bold"), bg="#1e1e2f", fg="white")
user_label.pack(pady=5)

comp_label = tk.Label(root, text="Computer: ", font=("Arial", 14, "bold"), bg="#1e1e2f", fg="white")
comp_label.pack(pady=5)

result_label = tk.Label(root, text="Let's Play! 😎", 
                        font=("Comic Sans MS", 16, "bold"), 
                        bg="#1e1e2f", fg="#ffcc00")
result_label.pack(pady=20)

# Exit button
exit_btn = tk.Button(root, text="🚪 Exit", font=("Arial", 12, "bold"),
                     bg="#ff3300", fg="white", width=10,
                     command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()
