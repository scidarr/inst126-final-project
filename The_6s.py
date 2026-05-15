import os
import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def display_leaderboard():
    """Displays the persistent leaderboard.txt file at the start of the game."""
    print("\n" + "="*40)
    print("TUPLE OUT: The 6s")
    print("="*40)
    # loop through all possible dice settings to show high scores
    for i in range(3, 7):
        print("--- " + str(i) + " Dice Leaderboard ---")
        filename = "leaderboard_" + str(i) + ".txt"
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
        print("")
    print("="*40 + "\n")

def get_num_dice():
    """Ask user for dice count and make sure it is a valid integer"""
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
    """Find unique values manually"""
    value_unique = []
    for val in dice_list:
        if val not in value_unique:
            value_unique.append(val)
            
    # check if value appears 2 or more times to fix it
    fixed_values = []
    for value in value_unique:
        if dice_list.count(value) >= 2:
            fixed_values.append(value)
    
    # create a true/false mask for the dice
    fixed_indices = []
    for val in dice_list:
        if val in fixed_values:
            fixed_indices.append(True)
        else:
            fixed_indices.append(False)
            
    return fixed_values, fixed_indices

def evaluate_tuples(dice_list, total_dice):
    """Find unique values to check counts"""
    value_unique = []
    for val in dice_list:
        if val not in value_unique:
            value_unique.append(val)
            
    # adjust tuple requirement based on total dice
    tuple_req = 3
    if total_dice >= 5:
        tuple_req = 4
            
    # check for super tuple (6s) or regular tuple out (1-5s)
    for value in value_unique:
        if dice_list.count(value) >= tuple_req:
            if value == 6:
                return "super_tuple"
            else:
                return "tuple_out"
    return "safe"

def play_turn(player_name, opponent_name, scores, total_dice):
    """Turn phase for User or Computer"""
    time.sleep(0.5)
    print(f"\n--- {player_name}'s Turn ---")
    current_dice = diceroll(total_dice)
    round_score = 0
    rerolls = 0
    
    # loop for re-rolling
    while True:
        time.sleep(0.5)
        print(f"\nRolled Dice: {current_dice}")
        status = evaluate_tuples(current_dice, total_dice)
        
        if status == "super_tuple":
            time.sleep(0.5)
            print("\n SUPER TUPLE ACTIVATED! Rolled three 6s!")
            penalty = 15
            scores[opponent_name] = max(0, scores[opponent_name] - penalty)
            round_score = sum(current_dice)
            print(f"Sabotage successful! {opponent_name} loses {penalty} points (Current score: {scores[opponent_name]}).")
            print(f"{player_name} automatically banks {round_score} points this round!")
            break    
            
        elif status == "tuple_out":
            time.sleep(0.5)
            print("\n Tupled Out!! Rolled three identical numbers (1-5).")
            print("Turn ends immediately. 0 points earned this round.")
            round_score = 0
            break       
            
        fixed_vals, fixed_mask = get_fixed_dice(current_dice)
        current_sum = sum(current_dice)
        if fixed_vals:
            print(f"Fixed values (cannot be rerolled): {fixed_vals}")
        else:
            print("No dice are currently fixed.")
        print(f"Current showing round total: {current_sum}")
        
        if all(fixed_mask):
            time.sleep(0.5)
            print("All dice are fixed! Automatically stopping and banking points.")
            round_score = current_sum
            break

        # check re-roll limit
        if rerolls >= 6:
            time.sleep(0.5)
            print("Re-roll limit reached! 10 point penalty and turn ends.")
            scores[player_name] -= 10
            if scores[player_name] < 0:
                scores[player_name] = 0
            round_score = 0
            break
            
        # determine next action based on human or AI
        if player_name != "AI":
            choice = ""
            while choice not in ["r", "s", "roll", "stop"]:
                choice = input("Do you want to re-roll unfixed dice or stop? (r/s): ").strip().lower()
                if choice not in ["r", "s", "roll", "stop"]:
                    print("Invalid input. Please type 'r' or 's'.")
                    
            if choice == "s" or choice == "stop":
                choice = "stop"
                round_score = current_sum
                print(f"{player_name} stops and successfully banks {round_score} points!")
                break
            elif choice == "r" or choice == "roll":
                choice = "roll"
        else:
            time.sleep(0.8)
            if current_sum < 12 and not all(fixed_mask):
                print("AI Decision: Showing total is less than 12. AI chooses to RE-ROLL.")
                choice = "roll"
            else:
                print("AI Decision: Target threshold reached. AI chooses to STOP.")
                round_score = current_sum
                print(f"AI successfully banks {round_score} points!")
                break
                
        # roll unfixed dice
        if choice == "roll":
            rerolls += 1
            new_rolls = diceroll(total_dice)
            for i in range(total_dice):
                if not fixed_mask[i]:
                    current_dice[i] = new_rolls[i]                
                    
    time.sleep(0.5)
    scores[player_name] += round_score
    print(f"End of turn update -> {player_name} Total Score: {scores[player_name]}")

def main():
    """Coordinates setup, scores, alternating game loops"""
    display_leaderboard()
    user_name = input("Enter your name: ")
    
    # game session loop
    while True:
        scores = {user_name: 0, "AI": 0}
        num_dice = get_num_dice()
        print("\nGame initialized with " + str(num_dice) + " dice. First to reach or exceed 60 points wins!")
        time.sleep(0.5)
        print("Lets get rolling...")
        time.sleep(0.5)
        print("----------------------------------------")
        score_history = []
        turn_number = 1
        
        # main match loop
        while True:
            time.sleep(0.5)
            print("\n=== ROUND " + str(turn_number) + " ===")
            
            # human turn
            play_turn(user_name, "AI", scores, num_dice)
            score_history.append({"Turn": turn_number, "Player": user_name, "Score": scores[user_name]})    
            
            # check human win
            if scores[user_name] >= 60:
                time.sleep(0.5)
                print("\n*******************************************")
                print("VICTORY! You win the game in " + str(turn_number) + " rounds!")
                print("*******************************************")
                with open("leaderboard_" + str(num_dice) + ".txt", "a") as file:
                    file.write("Winner: " + user_name + " | Rounds: " + str(turn_number) + "\n")
                print("Saved match results to leaderboard!")
                break     
                
            # ai turn
            play_turn("AI", user_name, scores, num_dice)
            score_history.append({"Turn": turn_number, "Player": "AI", "Score": scores["AI"]})
            
            # check ai win
            if scores["AI"] >= 60:
                time.sleep(0.5)
                print("\n****************************************")
                print("DEFEAT! Computer wins the game in " + str(turn_number) + " rounds.")
                print("****************************************")
                with open("leaderboard_" + str(num_dice) + ".txt", "a") as file:
                    file.write("Winner: AI | Rounds: " + str(turn_number) + "\n")
                print("Saved match results to leaderboard!")
                break
                
            time.sleep(0.5)
            print("\n------------------------------")
            print("Current Standings Round " + str(turn_number) + ":")
            print(f"{user_name}: {scores[user_name]} | AI: {scores['AI']}")
            print("------------------------------")
            turn_number += 1
            
        # display graph at the end of the match
        print("\nVisualizing game performance graph...")
        df = pd.DataFrame(score_history)
        plt.clf()
        sns.lineplot(data=df, x="Turn", y="Score", hue="Player")
        plt.title("Game Score")
        plt.show()
        
        display_leaderboard()
        
        # ask the user if they want to play again
        play_again = input("Go again? (y/n): ").strip().lower()
        if play_again != "y" and play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()