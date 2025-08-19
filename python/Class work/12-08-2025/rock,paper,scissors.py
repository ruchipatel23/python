import random

print("Welcome to Rock, Paper, Scissors Game")
print("Choices: rock, paper, scissors")

# User input
user_choice = input("Enter your choice: ").lower()

# Computer random choice
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print(f"Computer chose: {computer_choice}")


if user_choice == computer_choice:
    print("It's a tie")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print("You win!")
else:
    print("Computer wins")