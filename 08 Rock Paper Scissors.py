"""https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html"""

while True:
    player_1 = ""
    while player_1 == "":
        player_1 = input("Player One, Rock, Paper or Scissors?\nPlayer One>").lower()
        if player_1 != "rock" and player_1 != "paper" and player_1 != "scissors":
            player_1 = ""
            print("You can only input 'Rock', 'Paper' or 'Scissors'.")
    player_2 = ""
    while player_2 == "":
        player_2 = input("Player Two, Rock, Paper or Scissors?\nPlayer Two>").lower()
        if player_2 != "rock" and player_2 != "paper" and player_2 != "scissors":
            player_2 = ""
            print("You can only input 'Rock', 'Paper' or 'Scissors'.")
    if player_1 == player_2:
        print("It's a draw!")
    else:
        if player_1 == "rock" and player_2 == "scissors" or player_1 == "scissors"\
                and player_2 == "paper" or player_1 == "paper" and player_2 == "rock":
            print("Player One wins!! Well done!")
        else:
            print("Player Two wins!! Very good!")
    again = ""
    while again == "":
        again = input("Wanna play again?\n>").lower()
        if again != "yes" and again != "no":
            again = ""
            print("Just say 'yes' or 'no'")
        if again == "no":
            print("Goodbye~")
            quit()
        if again == "yes":
            print("Nice! Let's play again!")
