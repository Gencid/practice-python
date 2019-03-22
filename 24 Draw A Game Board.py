"""https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html"""


def give_number():
    while True:
        try:
            num = int(input("How big would you like this board?\n>"))
            if num < 1:
                print("Input an integer higher than 0, please")
                continue
            return num
        except ValueError:
            print("Input an integer, please.")


def draw_board(size):
    for row in range(0, size):
        print(" ---" * size)
        print("|   " * size + "|")
    print(" ---" * size)


print("Let's draw a game board!")
print("Give me a number A and I'll make a board of AxA size in cells.")
board_size = give_number()
print("Okay, here is the board!")
draw_board(board_size)
