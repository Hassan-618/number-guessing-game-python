"""
I acknowledge the use of ChatGPT (OpenAI, https://chat.openai.com/) 
to create the code in this file for the Number Guessing Game implementation.
"""

import random

class NumberGuessingGame:
    def __init__(self):
        self.target_number = 0
        self.attempts = 0
        self.max_attempts = 7
        self.min_range = 1
        self.max_range = 100
        
    def start_game(self):
        """Initialize a new game"""
        self.target_number = random.randint(self.min_range, self.max_range)
        self.attempts = 0
        print(f"\n🎮 Welcome to the Number Guessing Game!")
        print(f"I'm thinking of a number between {self.min_range} and {self.max_range}")
        print(f"You have {self.max_attempts} attempts to guess it!")
        
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

def play_game():
    """Main game loop with enhanced win/lose conditions"""
    game = NumberGuessingGame()
    games_played = 0
    games_won = 0
    
    print("🎯 Number Guessing Game - Enhanced Version")
    print("="*50)
    
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