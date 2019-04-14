"""https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html"""


def input_coords(player, board):
    # ---- Asking for inputs ----
    while True:
        inputer = ""
        if player == 1:
            inputer = input("Player one, where will you input your \33[31mX\33[0m?\n>")
        elif player == 2:
            inputer = input("Player two, where will you input your \33[34mO\33[0m?\n>")
        inputer.strip()
        # ---- Handling errors ----
        if len(inputer) < 3:
            print("I need a 'x,y' input, with three characters. Try again.")
            continue
        elif len(inputer) > 3:
            print("I need a 'x,y' input, with three characters. Try again.")
            continue
        elif inputer[1] != ",":
            print("I need a 'x,y' input. Try again. Don't forget the comma.")
            continue
        try:
            int(inputer[0])
            int(inputer[2])
        except ValueError:
            print("I need a 'x,y' input, with numbers. Try again.")
            continue
        if int(inputer[0]) < 1 or int(inputer[0]) > 3 or int(inputer[2]) < 1 or int(inputer[2]) > 3:
            print("I need a 'x,y' input with values between 1 and 3. Try again.")
            continue
        # ---- Drawing the coordinates ---
        coords = inputer.split(",")
        coordies = [0, 0]
        coordies[0] = int(coords[0]) - 1
        coordies[1] = int(coords[1]) - 1
        sign = ""
        if player == 1:
            sign = "X"
        elif player == 2:
            sign = "O"
        if board[coordies[0]][coordies[1]] == 0:
            board[coordies[0]][coordies[1]] = sign
            return board
        else:
            print("Those coordinates were already chosen! Try again")


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

squares = 0
print("Let's draw your Xs and Os! Input them as coordinates, where x is the rows and y is the columns.")
print("For example, 1,1 would be the top-left corner, and 3,3 would be the bottom-right corner")

while squares < 9:
    play = 1
    print(input_coords(play, game))
    squares += 1
    if squares == 9:
        break
    play = 2
    print(input_coords(play, game))
    squares += 1

print("All cells were filled!")
