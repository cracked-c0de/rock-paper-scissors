import random

def play_again():
    print(game())
    again = input("\nWould you like to play again? (Yes, No): ").capitalize()
    match again:
        case "Yes":
            return play_again()
        case "No":
            return "Have a Good Day! See you soon..."
        case _:
            return "Invalid option. Program finished!"

options = ["Rock", "Paper", "Scissors"]

def game():
    player = input("\nEnter your choice (Rock, Paper, Scissors): ").capitalize()
    computer = random.choice(options)
    win = "\nHooray! You Win!"
    lose = "\nYou Lose :(\nBest Luck in next game!"
    draw = "\nDraw\nLet's try again!"
    error = "\nInvalid option!"
    choices = f"\nYour choice {player}, Computer choice {computer}"
    if player in options:
        print(choices)
        if player == computer:
            return draw 
        elif player == options[0]:
            if computer == options[1]:
                return lose
            else:
                return win
        elif player == options[1]:
            if computer == options[0]:
                return win
            else:
                return lose
        else:
            if computer == options[1]:
                return lose
            else:
                return win
    else:
        return error


play = play_again()
print(play)