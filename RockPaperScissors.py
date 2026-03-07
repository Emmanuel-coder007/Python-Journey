import random
num = ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]
print("Welcome to Rock, Paper, Scissors!")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
print("4. Lizard")
print("5. Spock")
player = int(input("Enter your choice (1-5): "))
computer = random.randint(1, 5)

if player == computer:
    print(f"You chose {num[player - 1]} and the computer chose {num[computer - 1]}.")
    print("It's a tie!")    
elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2) or (player == 4 and computer == 5) or (player == 4 and computer == 2) or (player == 5 and computer == 3) or (player == 5 and computer == 1):
    print(f"You chose {num[player - 1]} and the computer chose {num[computer - 1]}.")
    print("You win!")
else:
    print(f"You chose {num[player - 1]} and the computer chose {num[computer - 1]}.")
    print("Computer wins!")