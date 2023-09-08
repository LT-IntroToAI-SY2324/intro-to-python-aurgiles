# We will write a rock paper scissors game in class - Complete it in this file

import random

player_choice = "rock"
computer_choice = "paper"

def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("enter a choice (rock, paper, scissors")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}


    return choices

def check_win(player, computer):
    print("you chose {player}, computer chose {computer}")
    if player == computer:

        return "its a tie"
    elif player == "rock":
        if computer == "scissors":
            return "rock smashes paper, you win!"
        else:
            return "paper covers rock, you lose."

result = check_win("scissors", "rock")
print(result)



choices = get_choices()
print(choices)