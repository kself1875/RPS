import random

print("Welcome to Rock, Paper, Scissors")
print("*********************************")

# prompt player for choice

player_choice = input("What is your choice?: 'rock', 'paper', 'scissors'")

# place possible choices in list rock, paper, scissors

possible_choices = ['rock', 'paper', 'scissors']

# computer chooses selection by using the random function from the random module
# computer randomly selects from the list
computer_choice = random.choice(possible_choices)

# show choices of user and cpu. format strings

print(f"You chose {player_choice}, Computer chose {computer_choice}. \n")

# Set rules for a winner
# rock > scissors, paper > rock, scissors > paper

if player_choice == computer_choice:
    print(f"You and the computer both selected {player_choice}. The game is a tie!")
elif player_choice == "rock":
    if computer_choice == "scissors":
        print("Rock destroys scissors! You win this round!")
    else:
        print("Paper covers rock! You lose this round!")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win this round!")
    else:
        print("Scissors slices and dices paper! You lose this round!")
elif player_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors slices and dices paper! You win this round!")
    else:
        print("Rock destroys scissors! You lose this round!")







