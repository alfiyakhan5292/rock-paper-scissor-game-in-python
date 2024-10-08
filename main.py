import random

options = ("rock","paper","scissors")
running = True

while running:

    computer = random.choice(options)
    player = None
    
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("Rock smashes scissors! You win!")
    elif player == "paper" and  computer == "rock":
        print("You win!")
    elif player == "scissors" and  computer == "paper":
        print("You win!")
    else:
        print("You lose!") 
    if not input("play again? (y/n): ").lower() == "y":
        running = False

print("Thank for playing!")
