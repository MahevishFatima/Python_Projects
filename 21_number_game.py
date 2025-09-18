import tkinter as tk
from tkinter import messagebox

# ---------- GAME LOGIC ----------
def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def check(xyz):
    for i in range(1, len(xyz)):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False
    return True

class Number21Game:
    def __init__(self, root):
        self.root = root
        self.root.title("21 Number Game 🎮")
        self.root.geometry("600x450")
        self.root.configure(bg="#282c34")

        self.xyz = []
        self.last = 0
        self.comp = 0
        self.player_turn = False

        # Title
        title = tk.Label(root, text="21 Number Game", font=("Arial", 20, "bold"),
                         fg="white", bg="#61afef")
        title.pack(fill=tk.X, pady=10)

        # Info Label
        self.info = tk.Label(root, text="Choose First or Second Turn",
                             font=("Arial", 14), fg="white", bg="#282c34")
        self.info.pack(pady=10)

        # Buttons for first/second
        self.btn_frame = tk.Frame(root, bg="#282c34")
        self.btn_frame.pack()
        tk.Button(self.btn_frame, text="First (F)", font=("Arial", 12, "bold"),
                  bg="#98c379", width=12, command=self.start_first).grid(row=0, column=0, padx=10)
        tk.Button(self.btn_frame, text="Second (S)", font=("Arial", 12, "bold"),
                  bg="#e5c07b", width=12, command=self.start_second).grid(row=0, column=1, padx=10)

        # Sequence display
        self.seq_label = tk.Label(root, text="Sequence: []", font=("Arial", 12),
                                  fg="#abb2bf", bg="#282c34", wraplength=550, justify="left")
        self.seq_label.pack(pady=15)

        # Number choice buttons
        self.choice_frame = tk.Frame(root, bg="#282c34")
        self.choice_buttons = []
        for i in range(1, 4):
            b = tk.Button(self.choice_frame, text=f"Enter {i}", font=("Arial", 12, "bold"),
                          bg="#c678dd", fg="white", width=10,
                          command=lambda n=i: self.player_move(n))
            b.grid(row=0, column=i-1, padx=8)
            self.choice_buttons.append(b)

    def update_sequence(self):
        self.seq_label.config(text=f"Sequence: {self.xyz}")

    def lose(self):
        messagebox.showerror("Game Over", "YOU LOSE!\nBetter luck next time 😢\n\n"
                                          "👉 Winning Strategy:\nAlways stop at 4, 8, 12, 16, 20.\n"
                                          "That way, opponent is forced to say 21!")
        self.root.quit()

    def win(self):
        messagebox.showinfo("Congratulations 🎉", "YOU WON! 🏆")
        self.root.quit()

    def start_first(self):
        self.info.config(text="Your Turn! Choose 1, 2 or 3 numbers")
        self.choice_frame.pack(pady=10)
        self.comp = 0
        self.xyz = []
        self.last = 0
        self.player_turn = True

    def start_second(self):
        self.info.config(text="Computer starts...")
        self.choice_frame.pack(pady=10)
        self.xyz = []
        self.last = 0
        self.comp = 1
        self.computer_move()

    def player_move(self, count):
        if not self.player_turn:
            return

        temp = []
        for i in range(count):
            temp.append(self.last + i + 1)

        self.xyz.extend(temp)
        self.last = self.xyz[-1]
        self.update_sequence()

        if not check(self.xyz):
            self.lose()

        if self.last >= 21:
            self.lose()

        # Computer's turn
        self.player_turn = False
        self.info.config(text="Computer's Turn...")
        self.root.after(1000, self.computer_move)

    def computer_move(self):
        if self.last >= 20:
            self.win()
            return

        if self.comp == 0:  # player first mode
            comp_count = 4 - (len(self.xyz) % 4)
            if comp_count == 4:
                comp_count = 3
        else:  # player second mode
            near = nearestMultiple(self.last)
            comp_count = near - self.last
            if comp_count == 4:
                comp_count = 3

        for i in range(1, comp_count + 1):
            self.xyz.append(self.last + i)
        self.last = self.xyz[-1]

        self.update_sequence()

        if self.last >= 21:
            self.lose()

        self.player_turn = True
        self.info.config(text="Your Turn! Choose 1, 2 or 3 numbers")


# ---------- RUN APP ----------
if __name__ == "__main__":
    root = tk.Tk()
    game = Number21Game(root)
    root.mainloop()
