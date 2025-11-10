"""
I acknowledge the use of ChatGPT (OpenAI, https://chat.openai.com/) 
to create the code in this file for the Number Guessing Game implementation.
"""

import random

class NumberGuessingGame:
    def __init__(self, difficulty="medium"):
        self.target_number = 0
        self.attempts = 0
        self.difficulty = difficulty
        self.set_difficulty(difficulty)
        
    def set_difficulty(self, difficulty):
        """Set game difficulty with different ranges and attempts"""
        difficulties = {
            "easy": {"min": 1, "max": 50, "attempts": 10},
            "medium": {"min": 1, "max": 100, "attempts": 7},
            "hard": {"min": 1, "max": 200, "attempts": 5}
        }
        
        if difficulty in difficulties:
            self.difficulty = difficulty
            self.min_range = difficulties[difficulty]["min"]
            self.max_range = difficulties[difficulty]["max"]
            self.max_attempts = difficulties[difficulty]["attempts"]
        else:
            # Default to medium
            self.difficulty = "medium"
            self.min_range = 1
            self.max_range = 100
            self.max_attempts = 7
        
    def start_game(self):
        """Initialize a new game"""
        self.target_number = random.randint(self.min_range, self.max_range)
        self.attempts = 0
        print(f"\n🎮 Welcome to the Number Guessing Game!")
        print(f"🎯 Difficulty: {self.difficulty.upper()}")
        print(f"📊 Range: {self.min_range} to {self.max_range}")
        print(f"🎲 Attempts: {self.max_attempts}")
        print(f"I'm thinking of a number between {self.min_range} and {self.max_range}")
        
    def make_guess(self, guess):
        """Process a player's guess and return feedback"""
        self.attempts += 1
        
        if guess == self.target_number:
            return "win"
        elif guess < self.target_number:
            return "too_low"
        else:
            return "too_high"
    
    def is_game_over(self):
        """Check if game is over (won or out of attempts)"""
        return self.attempts >= self.max_attempts
    
    def get_remaining_attempts(self):
        """Get number of remaining attempts"""
        return self.max_attempts - self.attempts

def select_difficulty():
    """Allow player to select difficulty level"""
    print("\n🎯 Select Difficulty Level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            if choice == 1:
                return "easy"
            elif choice == 2:
                return "medium"
            elif choice == 3:
                return "hard"
            else:
                print("❌ Please enter 1, 2, or 3")
        except ValueError:
            print("❌ Please enter a valid number")

def play_game():
    """Main game loop with difficulty selection"""
    print("🎯 Number Guessing Game - Enhanced Version")
    print("="*50)
    
    difficulty = select_difficulty()
    game = NumberGuessingGame(difficulty)
    games_played = 0
    games_won = 0
    
    while True:
        games_played += 1
        game.start_game()
        game_won = False
        
        while not game.is_game_over():
            try:
                guess = int(input(f"\nEnter your guess ({game.get_remaining_attempts()} attempts left): "))
                
                if guess < game.min_range or guess > game.max_range:
                    print(f"⚠️  Please enter a number between {game.min_range} and {game.max_range}")
                    continue
                
                result = game.make_guess(guess)
                
                if result == "win":
                    games_won += 1
                    game_won = True
                    score = max(100 - (game.attempts - 1) * 10, 10)
                    print(f"🎉 Congratulations! You guessed it in {game.attempts} attempts!")
                    print(f"🏆 Your score: {score} points")
                    break
                elif result == "too_low":
                    print("📈 Too low! Try a higher number.")
                elif result == "too_high":
                    print("📉 Too high! Try a lower number.")
                    
            except ValueError:
                print("❌ Please enter a valid number!")
        
        # Game over conditions
        if not game_won:
            print(f"💀 Game Over! The number was {game.target_number}")
            print("🎯 Better luck next time!")
        
        # Display statistics
        win_rate = (games_won / games_played) * 100
        print(f"\n📊 Statistics: {games_won}/{games_played} games won ({win_rate:.1f}% win rate)")
        
        # Ask to play again
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"\n🎮 Final Statistics:")
            print(f"   Games Played: {games_played}")
            print(f"   Games Won: {games_won}")
            print(f"   Win Rate: {win_rate:.1f}%")
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    play_game()