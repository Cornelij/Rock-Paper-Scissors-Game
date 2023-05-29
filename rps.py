import random

user_action = input("Enter a choice (rock, paper, or scissors):").lower()
possible_moves = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_moves)

print(f"\nYou Chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print(f"Rock smashes scissors! You win!")
    else:
        print(f"Paper covers Rock! You loose!")
elif user_action == "paper":
    if computer_action == "rock":
        print(f"Paper covers Rock! You win!")
    else:
        print("Scissors cuts paper! You lose!")
elif user_action == "scissors":
    if computer_action == "paper":
        print(f"Scissors cuts Paper!, You win!")
    else:
        print(f"Rock smashes Scissors! You lose.")