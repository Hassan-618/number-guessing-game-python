"""
I acknowledge the use of ChatGPT (OpenAI, https://chat.openai.com/) 
to create the code in this file for the Number Guessing Game implementation.
"""

import tkinter as tk
from tkinter import messagebox, ttk
import random

class NumberGuessingGameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Number Guessing Game")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Game variables
        self.target_number = 0
        self.attempts = 0
        self.max_attempts = 7
        self.min_range = 1
        self.max_range = 100
        self.difficulty = "medium"
        self.games_played = 0
        self.games_won = 0
        
        self.setup_ui()
        self.new_game()
        
    def setup_ui(self):
        """Create the GUI interface"""
        # Title
        title_label = tk.Label(self.root, text="🎯 Number Guessing Game", 
                              font=("Arial", 16, "bold"), fg="blue")
        title_label.pack(pady=10)
        
        # Difficulty selection
        difficulty_frame = tk.Frame(self.root)
        difficulty_frame.pack(pady=10)
        
        tk.Label(difficulty_frame, text="Difficulty:", font=("Arial", 10, "bold")).pack()
        self.difficulty_var = tk.StringVar(value="medium")
        
        difficulties = [("Easy (1-50, 10 attempts)", "easy"),
                       ("Medium (1-100, 7 attempts)", "medium"),
                       ("Hard (1-200, 5 attempts)", "hard")]
        
        for text, value in difficulties:
            tk.Radiobutton(difficulty_frame, text=text, variable=self.difficulty_var,
                          value=value, command=self.change_difficulty).pack(anchor="w")
        
        # Game info
        self.info_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.info_label.pack(pady=10)
        
        # Input section
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Enter your guess:", font=("Arial", 10)).pack()
        self.guess_entry = tk.Entry(input_frame, font=("Arial", 12), width=10, justify="center")
        self.guess_entry.pack(pady=5)
        self.guess_entry.bind("<Return>", lambda e: self.make_guess())
        
        self.submit_button = tk.Button(input_frame, text="Submit Guess", 
                                     command=self.make_guess, font=("Arial", 10, "bold"),
                                     bg="lightblue")
        self.submit_button.pack(pady=5)
        
        # Feedback section
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"))
        self.feedback_label.pack(pady=10)
        
        # Attempts counter
        self.attempts_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.attempts_label.pack()
        
        # Statistics
        self.stats_label = tk.Label(self.root, text="", font=("Arial", 9))
        self.stats_label.pack(pady=10)
        
        # Control buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        self.new_game_button = tk.Button(button_frame, text="New Game", 
                                       command=self.new_game, font=("Arial", 10),
                                       bg="lightgreen")
        self.new_game_button.pack(side="left", padx=5)
        
        quit_button = tk.Button(button_frame, text="Quit", 
                              command=self.root.quit, font=("Arial", 10),
                              bg="lightcoral")
        quit_button.pack(side="left", padx=5)
        
    def change_difficulty(self):
        """Change game difficulty"""
        self.difficulty = self.difficulty_var.get()
        difficulties = {
            "easy": {"min": 1, "max": 50, "attempts": 10},
            "medium": {"min": 1, "max": 100, "attempts": 7},
            "hard": {"min": 1, "max": 200, "attempts": 5}
        }
        
        settings = difficulties[self.difficulty]
        self.min_range = settings["min"]
        self.max_range = settings["max"]
        self.max_attempts = settings["attempts"]
        
        self.new_game()
        
    def new_game(self):
        """Start a new game"""
        self.target_number = random.randint(self.min_range, self.max_range)
        self.attempts = 0
        self.games_played += 1
        
        self.info_label.config(text=f"Guess a number between {self.min_range} and {self.max_range}")
        self.feedback_label.config(text="Good luck! 🍀", fg="black")
        self.update_attempts_display()
        self.update_stats()
        
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()
        self.submit_button.config(state="normal")
        
    def make_guess(self):
        """Process player's guess"""
        try:
            guess = int(self.guess_entry.get())
            
            if guess < self.min_range or guess > self.max_range:
                self.feedback_label.config(text=f"Please enter a number between {self.min_range} and {self.max_range}!", 
                                         fg="orange")
                return
                
            self.attempts += 1
            
            if guess == self.target_number:
                self.games_won += 1
                score = max(100 - (self.attempts - 1) * 10, 10)
                self.feedback_label.config(text=f"🎉 Congratulations! Score: {score}", fg="green")
                self.submit_button.config(state="disabled")
                messagebox.showinfo("You Won!", f"Congratulations! You guessed it in {self.attempts} attempts!\\nScore: {score} points")
            elif guess < self.target_number:
                self.feedback_label.config(text="📈 Too low! Try higher.", fg="blue")
            else:
                self.feedback_label.config(text="📉 Too high! Try lower.", fg="red")
                
            self.update_attempts_display()
            
            if self.attempts >= self.max_attempts and guess != self.target_number:
                self.feedback_label.config(text=f"💀 Game Over! Number was {self.target_number}", fg="red")
                self.submit_button.config(state="disabled")
                messagebox.showinfo("Game Over", f"Sorry! The number was {self.target_number}")
                
            self.update_stats()
            self.guess_entry.delete(0, tk.END)
            
        except ValueError:
            self.feedback_label.config(text="❌ Please enter a valid number!", fg="red")
            
    def update_attempts_display(self):
        """Update attempts counter"""
        remaining = self.max_attempts - self.attempts
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts} (Remaining: {remaining})")
        
    def update_stats(self):
        """Update game statistics"""
        if self.games_played > 0:
            win_rate = (self.games_won / self.games_played) * 100
            self.stats_label.config(text=f"📊 Games: {self.games_played} | Won: {self.games_won} | Win Rate: {win_rate:.1f}%")
        
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()

if __name__ == "__main__":
    game = NumberGuessingGameGUI()
    game.run()