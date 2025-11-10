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
        self.root.geometry("1080x1080")
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
        self.game_over = False
        self.game_won = False
        
        self.setup_ui()
        self.start_first_game()
        
    def setup_ui(self):
        """Create the GUI interface"""
        # Title
        title_label = tk.Label(self.root, text="🎯 Number Guessing Game", 
                              font=("Arial", 18, "bold"), fg="darkblue", bg="lightgray")
        title_label.pack(pady=15, fill="x")
        
        # Difficulty selection
        difficulty_frame = tk.LabelFrame(self.root, text="Select Difficulty", 
                                       font=("Arial", 11, "bold"), fg="darkgreen")
        difficulty_frame.pack(pady=10, padx=20, fill="x")
        
        self.difficulty_var = tk.StringVar(value="medium")
        
        difficulties = [("Easy (1-50, 10 attempts)", "easy"),
                       ("Medium (1-100, 7 attempts)", "medium"),
                       ("Hard (1-200, 5 attempts)", "hard")]
        
        for text, value in difficulties:
            tk.Radiobutton(difficulty_frame, text=text, variable=self.difficulty_var,
                          value=value, command=self.change_difficulty, 
                          font=("Arial", 10)).pack(anchor="w", padx=10, pady=2)
        
        # Game info
        info_frame = tk.Frame(self.root, bg="lightyellow", relief="ridge", bd=2)
        info_frame.pack(pady=10, padx=20, fill="x")
        self.info_label = tk.Label(info_frame, text="", font=("Arial", 11, "bold"), 
                                 bg="lightyellow", fg="darkblue")
        self.info_label.pack(pady=8)
        
        # Input section
        input_frame = tk.LabelFrame(self.root, text="Make Your Guess", 
                                  font=("Arial", 11, "bold"), fg="darkred")
        input_frame.pack(pady=15, padx=20, fill="x")
        
        tk.Label(input_frame, text="Enter your guess:", font=("Arial", 10)).pack(pady=5)
        self.guess_entry = tk.Entry(input_frame, font=("Arial", 14, "bold"), width=12, 
                                  justify="center", relief="sunken", bd=2)
        self.guess_entry.pack(pady=8)
        self.guess_entry.bind("<Return>", lambda e: self.make_guess())
        
        self.submit_button = tk.Button(input_frame, text="Submit Guess", 
                                     command=self.make_guess, font=("Arial", 11, "bold"),
                                     bg="lightblue", width=12, relief="raised")
        self.submit_button.pack(pady=8)
        
        # Feedback section
        feedback_frame = tk.Frame(self.root, bg="white", relief="groove", bd=2)
        feedback_frame.pack(pady=10, padx=20, fill="x")
        self.feedback_label = tk.Label(feedback_frame, text="", font=("Arial", 12, "bold"), 
                                     bg="white", height=2)
        self.feedback_label.pack(pady=10)
        
        # Attempts counter
        attempts_frame = tk.Frame(self.root, bg="lightcyan", relief="ridge", bd=1)
        attempts_frame.pack(pady=5, padx=20, fill="x")
        self.attempts_label = tk.Label(attempts_frame, text="", font=("Arial", 10, "bold"), 
                                     bg="lightcyan", fg="darkblue")
        self.attempts_label.pack(pady=5)
        
        # Statistics
        stats_frame = tk.Frame(self.root, bg="lightgray", relief="ridge", bd=1)
        stats_frame.pack(pady=5, padx=20, fill="x")
        self.stats_label = tk.Label(stats_frame, text="", font=("Arial", 10, "bold"), 
                                  bg="lightgray", fg="darkgreen")
        self.stats_label.pack(pady=5)
        
        # Control buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=25)
        
        self.new_game_button = tk.Button(button_frame, text="New Game", 
                                       command=self.start_new_game, font=("Arial", 10, "bold"),
                                       bg="lightgreen", width=10)
        self.new_game_button.pack(side="left", padx=5)
        
        quit_button = tk.Button(button_frame, text="Quit", 
                              command=self.root.quit, font=("Arial", 10, "bold"),
                              bg="lightcoral", width=10)
        quit_button.pack(side="left", padx=5)
        
    def start_new_game(self):
        """Start a completely new game (called by New Game button)"""
        self.games_played += 1
        self.target_number = random.randint(self.min_range, self.max_range)
        self.attempts = 0
        self.game_over = False
        self.game_won = False
        
        self.info_label.config(text=f"Guess a number between {self.min_range} and {self.max_range}")
        self.feedback_label.config(text="Good luck! 🍀", fg="black")
        self.update_attempts_display()
        self.update_stats()
        
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.config(state="normal")
        self.guess_entry.focus()
        self.submit_button.config(state="normal")
        
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
        
        # Only start new game if not in middle of current game
        if self.game_over or self.attempts == 0:
            self.new_game()
        else:
            # Just update the display for current game
            self.info_label.config(text=f"Guess a number between {self.min_range} and {self.max_range}")
        
    def start_first_game(self):
        """Start the very first game without incrementing games_played"""
        self.target_number = random.randint(self.min_range, self.max_range)
        self.attempts = 0
        self.game_over = False
        self.game_won = False
        
        self.info_label.config(text=f"Guess a number between {self.min_range} and {self.max_range}")
        self.feedback_label.config(text="Good luck! 🍀", fg="black")
        self.update_attempts_display()
        self.update_stats()
        
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()
        self.submit_button.config(state="normal")
        
    def new_game(self):
        """Start a new game"""
        self.target_number = random.randint(self.min_range, self.max_range)
        self.attempts = 0
        self.game_over = False
        self.game_won = False
        
        # Only increment games_played when actually starting a new game
        if not hasattr(self, '_first_game_started'):
            self._first_game_started = True
        else:
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
        # Check if game is already over
        if self.game_over:
            self.feedback_label.config(text="🔄 Game finished! Click 'New Game' to play again.", fg="purple")
            return
            
        # Get and validate input
        guess_text = self.guess_entry.get().strip()
        if not guess_text:
            self.feedback_label.config(text="❌ Please enter a number!", fg="red")
            return
            
        try:
            guess = int(guess_text)
            
            if guess < self.min_range or guess > self.max_range:
                self.feedback_label.config(text=f"⚠️ Enter a number between {self.min_range} and {self.max_range}!", 
                                         fg="orange")
                self.guess_entry.delete(0, tk.END)
                return
                
            self.attempts += 1
            
            if guess == self.target_number:
                # Player won!
                self.games_won += 1
                self.game_over = True
                self.game_won = True
                score = max(100 - (self.attempts - 1) * 10, 10)
                self.feedback_label.config(text=f"🎉 Congratulations! Score: {score}", fg="green")
                self.submit_button.config(state="disabled")
                self.guess_entry.config(state="disabled")
                messagebox.showinfo("You Won!", f"Congratulations! You guessed it in {self.attempts} attempts!\nScore: {score} points")
                
            elif guess < self.target_number:
                self.feedback_label.config(text="📈 Too low! Try higher.", fg="blue")
            else:
                self.feedback_label.config(text="📉 Too high! Try lower.", fg="red")
                
            self.update_attempts_display()
            
            # Check if out of attempts
            if self.attempts >= self.max_attempts and not self.game_won:
                self.game_over = True
                self.feedback_label.config(text=f"💀 Game Over! Number was {self.target_number}", fg="red")
                self.submit_button.config(state="disabled")
                self.guess_entry.config(state="disabled")
                messagebox.showinfo("Game Over", f"Sorry! The number was {self.target_number}")
                
            self.update_stats()
            self.guess_entry.delete(0, tk.END)
            
        except ValueError:
            self.feedback_label.config(text="❌ Please enter a valid number!", fg="red")
            self.guess_entry.delete(0, tk.END)
            
    def update_attempts_display(self):
        """Update attempts counter"""
        remaining = self.max_attempts - self.attempts
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts} (Remaining: {remaining})")
        
    def update_stats(self):
        """Update game statistics"""
        if self.games_played > 0:
            win_rate = (self.games_won / self.games_played) * 100
            self.stats_label.config(text=f"📊 Games: {self.games_played} | Won: {self.games_won} | Win Rate: {win_rate:.1f}%")
        else:
            self.stats_label.config(text="📊 Games: 0 | Won: 0 | Win Rate: 0.0%")
        
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()

if __name__ == "__main__":
    game = NumberGuessingGameGUI()
    game.run()