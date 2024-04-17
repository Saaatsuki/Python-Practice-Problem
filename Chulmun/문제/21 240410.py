import random

def play_RockPaperScissor ():
    your_choice = input("Let's play Rock-Paper-Scissors✊✋✌ : " )

    choices = ["Rock✊","Paper✋","Scissors✌"]
    computer_choice = random.choice(choices)

    print("Conputer chose : ",computer_choice)

    if (((your_choice == "Rock")and(computer_choice == "Rock✊")) or 
          ((your_choice == "Paper")and(computer_choice == "Paper✋")) or 
          ((your_choice == "Scissors")and(computer_choice == "Scissors✌"))):
        print("Draw. Let's play rock-paper-scissors again.🎌")
        return play_RockPaperScissor()
        
    elif (((your_choice == "Rock")and(computer_choice == "Paper✋")) or 
          ((your_choice == "Paper")and(computer_choice == "Scissors✌")) or 
          ((your_choice == "Scissors")and(computer_choice == "Rock✊"))):
        print ("I win! You lose!!!🤡 Please challenge again!")
        return play_RockPaperScissor()
        
    elif (((your_choice == "Paper")and(computer_choice == "Rock✊")) or 
          ((your_choice == "Rock")and(computer_choice == "Scissors✌")) or 
          ((your_choice == "Scissors")and(computer_choice == "Paper✋"))):
        print ("Congratulations!!!You win!!!🐼🐼🐼❤️❤️❤️")
        
play_RockPaperScissor()
