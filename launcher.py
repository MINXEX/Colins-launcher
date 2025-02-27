import tkinter as tk
from tkinter import messagebox

class GameLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Colin's Launcher")
        self.root.geometry("400x300")
        self.root.configure(bg="#2E2E2E")

        # Title Label
        self.title_label = tk.Label(self.root, text="Colin's Launcher", font=("Helvetica", 24), bg="#2E2E2E", fg="#FFFFFF")
        self.title_label.pack(pady=20)

        # Button to Launch a Game
        self.launch_button = tk.Button(self.root, text="Launch Game", command=self.launch_game, bg="#5BBF26", fg="#FFFFFF", font=("Helvetica", 14))
        self.launch_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", command=root.quit, bg="#BF2626", fg="#FFFFFF", font=("Helvetica", 14))
        self.exit_button.pack(pady=10)

    def launch_game(self):
        messagebox.showinfo("Launch Game", "Launching your game!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GameLauncher(root)
    root.mainloop()