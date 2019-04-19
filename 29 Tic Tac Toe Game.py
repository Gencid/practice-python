"""https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html"""

from Functions.FTicTacToeGame import *

victoryX = 0
victoryO = 0

print("Let's draw a game board!")
print("Give me a number N and I'll make a board of NxN size in cells.")
if __name__ == "__main__":
    board_size = give_number()
    print("Okay, here is the board!")
    draw_board(board_size)
    if board_size == 3:
        print("Nice, a 3x3 board! Now you can play Tic Tac Toe!")
    else:
        print("That's a neat board, but you could play Tic Tac Toe if we drew a 3x3 one...")
        quit()

while True:
    game = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    squares = 0
    print("Let's draw your Xs and Os! Input them as coordinates, where x is the rows and y is the columns.")
    print("For example, 1,1 would be the top-left corner, and 3,3 would be the bottom-right corner.")
    while squares < 9:
        play = 1
        input_coords(play, game)
        print(" --- --- --- ")
        print("| " + game[0][0] + " | " + game[0][1] + " | " + game[0][2] + " |")
        print(" --- --- --- ")
        print("| " + game[1][0] + " | " + game[1][1] + " | " + game[1][2] + " |")
        print(" --- --- --- ")
        print("| " + game[2][0] + " | " + game[2][1] + " | " + game[2][2] + " |")
        print(" --- --- --- ")
        squares += 1
        if who_won(check_win(game)) == 1:
            victoryX += 1
            break
        if squares == 9:
            print("All cells were filled! It's a tie!")
            break
        play = 2
        input_coords(play, game)
        print("--- --- ---")
        print(" " + game[0][0] + " | " + game[0][1] + " | " + game[0][2] + " ")
        print("--- --- ---")
        print(" " + game[1][0] + " | " + game[1][1] + " | " + game[1][2] + " ")
        print("--- --- ---")
        print(" " + game[2][0] + " | " + game[2][1] + " | " + game[2][2] + " ")
        print("--- --- ---")
        squares += 1
        if who_won(check_win(game)) == 2:
            victoryO += 1
            break
    yesno = ""
    winner = ""
    print("Player 1 has won", victoryX, "times. Player 2 has won", victoryO, "times.")
    if victoryX > victoryO:
        print("Player 1 is on the lead! Will Player 2 want a rematch?")
        winner = "Player 1"
    elif victoryO > victoryX:
        print("Player 2 is on the lead! Will Player 1 want a rematch?")
        winner = "Player 2"
    while yesno == "":
        yesno = input("Do you want to play again?\n>").lower()
        if yesno == "yes" or yesno == "y":
            print("Great, let's play again!")
        elif yesno == "no" or yesno == "n":
            if victoryO == victoryX:
                print("But... both players are tied! There is no winner! Oh well.")
            else:
                print("And the winner is " + winner + "! Congratulations!")
            print("Let's play again any other time. Bye!")
            quit()
        else:
            print("Input yes/y or no/n, please.")
            yesno = ""
            continue
