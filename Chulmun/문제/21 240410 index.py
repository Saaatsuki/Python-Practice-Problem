import random

def play_RockPaperScissor():
    your_choice_index = int(input("Let's play Rock-Paper-Scissors✊✋✌ (Enter 0 for Rock, 1 for Paper, 2 for Scissors): "))

    choices = ["Rock✊", "Paper✋", "Scissors✌"]
    computer_choice_index = random.randint(0, 2)
    computer_choice = choices[computer_choice_index]

    print("Computer chose:", computer_choice)

    if your_choice_index == computer_choice_index:
        print("Draw. Let's play rock-paper-scissors again.🎌")
        return play_RockPaperScissor()

    elif (your_choice_index == 0 and computer_choice_index == 1) or \
         (your_choice_index == 1 and computer_choice_index == 2) or \
         (your_choice_index == 2 and computer_choice_index == 0):
        print("I win! You lose!!!🤡 Please challenge again!")
        return play_RockPaperScissor()

    else:
        print("Congratulations!!! You win!!!🐼🐼🐼❤️❤️❤️")

play_RockPaperScissor()
