import os
import numpy as np  #random number generation

def display_leaderboard():
    """Displays the persistent leaderboard.txt file at the start of the game."""
    print("\n" + "="*40)
    print("TUPLE OUT: The 6s")
    print("="*40)
    
    filename = "leaderboard.txt"
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                contents = file.read()
                if contents.strip():
                    print(contents)
                else:
                    print("No champions recorded yet. Be the first!")
        except Exception as e:
            print(f"Error reading leaderboard: {e}")
    else:
        print("No prior leaderboard found. A new one will be created upon winning.")
    print("="*40 + "\n")

def get_num_dice():
    """Prompts the player to choose the number of dice"""
    while True:
        try:
            choice = input("Choose how many dice to play (3-6): ").strip()
            num = int(choice)
            if 3 <= num <= 6:
                return num
            else:
                print("Invalid range. Please enter a number between 3 and 6.")
        except ValueError:
            print("Invalid input. Please type a valid number.")

def roll_dice(num_dice):
    """Generates random integers between 1 and 6 using NumPy"""
    # numpy.random.randint(low, high) evaluates [low, high) interval
    return np.random.randint(1, 7, size=num_dice).tolist()
