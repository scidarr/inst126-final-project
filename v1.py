import os
import numpy as np

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

def diceroll(num_dice):
    """Generates random integers between 1 and 6 using NumPy"""
    return np.random.randint(1, 7, size=num_dice).tolist()

def get_fixed_dice(dice_list):
    """Identifies values that appear at least twice in the roll, marking them as 'fixed'.
    Demonstrates Pattern 7.1 (Lists) and Pattern 6.2 (for-loop)."""
    value_unique = []
    for val in dice_list:
        if val not in value_unique:
            value_unique.append(val)
            
    fixed_values = []
    for value in value_unique:
        if dice_list.count(value) >= 2:
            fixed_values.append(value)
    
    fixed_indices = []
    for val in dice_list:
        if val in fixed_values:
            fixed_indices.append(True)
        else:
            fixed_indices.append(False)
            
    return fixed_values, fixed_indices

def evaluate_tuples(dice_list):
    """Checks if three dice share the exact same value.
    Returns status: 'super_tuple' (three 6s), 'tuple_out' (three 1-5s), or 'safe'.
    Demonstrates Pattern 5.1/5.3 (if/elif/else blocks)."""
    value_unique = []
    for val in dice_list:
        if val not in value_unique:
            value_unique.append(val)
            
    for value in value_unique:
        if dice_list.count(value) >= 3:
            if value == 6:
                return "super_tuple"  #Skips opponent turn if 3 6s
            else:
                return "tuple_out"    #0 pts
    return "safe"