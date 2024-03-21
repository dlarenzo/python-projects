import random

player_choice = int(input("Welcome to Rock, Paper, Scissors.  What do you choose? Type O for Rock, 1 for Paper, or 2 for  Scissors. "))

computer_choice = random.randint(0, 2)

if player_choice == 0 and computer_choice == 2:
    print(f"You win! You chose {player_choice}. The computer chose {computer_choice}")
elif player_choice == 2 and computer_choice == 1:
    print(f"You win! You chose {player_choice}. The computer chose {computer_choice}")
elif player_choice == 1 and computer_choice == 0:
    print(f"You win! You chose {player_choice}. The computer chose {computer_choice}")
elif player_choice == computer_choice:
    print(f"It's a draw! You chose {player_choice}. The computer chose {computer_choice}")
else:
    print(f"You lose! You chose {player_choice}. The computer chose {computer_choice}")