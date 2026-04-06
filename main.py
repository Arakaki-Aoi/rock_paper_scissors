import random
import tkinter as tk
from tkinter import ttk

hands_list = ["rock", "paper", "scissors"]


def generate_cpu_hand():
    return random.choice(hands_list)


def compare_hands(cpu_hand, user_hand):
    if cpu_hand == user_hand:
        return "tie"
    if (
        (cpu_hand == "rock" and user_hand == "scissors")
        or (cpu_hand == "paper" and user_hand == "rock")
        or (cpu_hand == "scissors" and user_hand == "paper")
    ):
        return "lose"
    return "win"


def outcome_message(result):
    if result == "tie":
        return "We're Even!"
    if result == "lose":
        return "You lose!"
    return "You win"


def create_game_window():
    print("Game start!")
    cpu_hand = generate_cpu_hand()

    root = tk.Tk()
    root.title("Rock Paper Scissors")
    user_hand = tk.StringVar()

    def select_hand():
        if user_hand.get():
            root.destroy()
        else:
            print("Please select your hand")

    combobox = ttk.Combobox(
        root,
        values=hands_list,
        textvariable=user_hand,
        state="readonly",
        width=30,
    )
    combobox.pack(padx=80, pady=(50, 20))
    button = tk.Button(root, text="Select", command=select_hand)
    button.pack(pady=(0, 40))

    root.update_idletasks()

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    window_w = root.winfo_width()
    window_h = root.winfo_height()

    x = (screen_w // 2) - (window_w // 2)
    y = (screen_h // 2) - (window_h // 2)

    root.geometry(f"{window_w}x{window_h}+{x}+{y}")
    root.mainloop()

    print(outcome_message(compare_hands(cpu_hand, user_hand.get())))


if __name__ == "__main__":
    create_game_window()