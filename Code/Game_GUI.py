import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.number_to_guess = random.randrange(100)
        self.chances = 7
        self.guess_counter = 0
        
        self.label = tk.Label(root, text="Guess a number between 0 and 99", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=5)
        
        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 12))
        self.button.pack(pady=5)
        
        self.feedback = tk.Label(root, text="You have 7 chances", font=("Arial", 12))
        self.feedback.pack(pady=10)
    
    def check_guess(self):
        try:
            my_guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
        
        self.guess_counter += 1
        if my_guess == self.number_to_guess:
            messagebox.showinfo("Congratulations!", f"The number is {self.number_to_guess}. You guessed it in {self.guess_counter} attempts!")
            self.root.quit()
        elif self.guess_counter >= self.chances:
            messagebox.showerror("Game Over", f"Oops, the number was {self.number_to_guess}. Better luck next time!")
            self.root.quit()
        elif my_guess > self.number_to_guess:
            self.feedback.config(text=f"Your guess is too high! {self.chances - self.guess_counter} chances left.")
        else:
            self.feedback.config(text=f"Your guess is too low! {self.chances - self.guess_counter} chances left.")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()