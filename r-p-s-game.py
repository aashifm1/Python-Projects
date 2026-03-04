
# This is rock, paper, scissors game

import random

choices = ["rock","paper","scissors"]
computer = random.choice(choices)

player = input("Choose rock, paper, scissors: ").lower()

# The winning condition
winner = {
    "rock":"scissors",
    "paper":"rock",
    "scissors":"paper"
}

if player == computer:
    print("It's a draw")
elif winner.get(player) == computer:
    print("You Win!")
else:
    print("Computer Wins!")