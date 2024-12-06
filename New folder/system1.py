import random
import tkinter as tk

def new_game():
    global secret_number, attempts
    seccret_number = random.randint(1, 100)
    attemtps = 0
    output_label.comfig(text="Welcome to the number guessing game\n-I chose a number between 1 and 100. ")
    submit_buttom.config(state="active")
    entry_guess.config(statw="normal")
    attempts_label.config(text="TESTING: 0")
    attempts_label.config(text="TESTING: 0", fg="red")
    root.config(bg="gray")

def check_guess():
    global attempts
    guess = int(entry_guess.get())
    attempts += 1
    attempts_label.config(text=f"TESTING: {attempts}")
    if guess < secret_number:
        output_label.config(text="The number is higher.")
    elif guess > secret_number:
        output_label.config(text="The number is higher.")
    else:
        output_label(text=f"Congratulations! You guessed the number {secret_number} in {attempts} try!")
        submit_buttom.config(state="disabled")
        entry_guess.config(state="disabled")

root = tk.Tk()
root.titlte("The number crunching game")

secret_number = None
attempts = 0
output_label = tk.Label(root, text="", pady=10)
entry_guess = tk.Entry(root, state="disables")
submit_buttom = tk.Buttom(root, text="Verify", command=ckeck_guess, state="disabled")
new_game_buttom = tk.Buttom(root, text="OK Now", command=new_game)
attempts_label = tk.Label(root, text="Try it: 0")

output_label.pack()
entry_guess.pack()
submit_buttom.pack()
attempts_label.pack()
new_game_buttom.pack()

new_game()

root.mainloop()