import random
def get_choices():
    player_choice = input("Enter a choice (Rock, Paper, Scissors): ").capitalize()
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    
    if player == computer:
        return "It's a tie!"
    
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose!"
    
    elif player == "Paper":
        if computer == "Rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose!"
    
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose!"
    else:
        return "Invalid input. Please choose Rock, Paper, or Scissors."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)