# Tuple Out: The 6s
## Darren Chung

## General
Tuple out: The 6s is a turn based dice game that allows you to play against a Computer opponent, fighting to be the first to reach 60 points. You can choose to play with 3 dice, or all the way up to 6 dice. Try to push your luck and bank those points!

## Setup
To play, you have to install Python on your computer. The libraries used in this game consist of numpy, pandas, matplotlib, and seaborn. Just open your terminal and run "pip install numpy pandas matplotlib seaborn". To launch the game, navigate to the folder where the game file is located. Run the file by typing "python The_6s.py", and you're all done!

## How to play
### Player Reroll
At the start, you will choose how many dice you want to play with (3-6). Player alternate turns with the computer. You will first roll and you can choose to re-roll (by typing 'r') any remaining dice that are not fixed to try and bank a higher score. You can stop at any point by typing 's' to avoid tupling out. The sum of all dice will be banked and added to your total game score. You are allowed a maximum of 6 re-rolls. If you hit the limit, a 10 point penalty will be applied and your turn ends.
### Tupling Out
When 3 (or more with more dice) are rolled, you will tuple out, automatically losing the turn and all the points on that round. Hint: Try to bank points early game to play around with higher round total and get Super Tuples later in the game.
### Super Tuple
Rolling 3 (or more with more dice) of 6s, does not make you tuple up. Instead, it sabotages your opponent! Your opponent will lose 15 points (score will not drop below 0). This is a game winning move so try your luck when you are about to lose!
### Computer AI
The Computer will use a risk evaluation strategy everytime they roll, and they will play it fairly safe. It will auto re-roll if the round total is less than 12 points (if there are unfixed dice). Try to use this to your advantage and go for totals above 12.
### Winning
The first side to reach 60 points will win the game. The highest total will be inserted to the leaderboard. There are multiple leader boards, each for different dice amounts. Will you be able to reach the top?