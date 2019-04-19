def check_win(board):
    result = 0
    for row in range(0, 3):
        if board[row][0] == board[row][1] and board[row][0] == board[row][2]:
            if board[row][0] == "X":
                result = 1
            elif board[row][0] == "O":
                result = 2
    for column in range(0, 3):
        if board[0][column] == board[1][column] and board[0][column] == board[2][column]:
            if board[0][column] == "X":
                result = 1
            elif board[0][column] == "O":
                result = 2
    if board[1][1] == board[0][0] and board[1][1] == board[2][2]:
        if board[1][1] == "X":
            result = 1
        elif board[1][1] == "O":
            result = 2
    elif board[1][1] == board[0][2] and board[1][1] == board[2][0]:
        if board[1][1] == "X":
            result = 1
        elif board[1][1] == "O":
            result = 2
    return result


def who_won(results):
    if results == 1:
        print("Player 1 won! Well done!")
        return 1
    elif results == 2:
        print("Player 2 won! Well done!")
        return 2


def input_coords(player, board):
    # ---- Asking for inputs ----
    while True:
        inputer = ""
        if player == 1:
            inputer = input("Player 1, where will you input your \33[31mX\33[0m?\n>")
        elif player == 2:
            inputer = input("Player 3, where will you input your \33[34mO\33[0m?\n>")
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
        if board[coordies[0]][coordies[1]] == " ":
            board[coordies[0]][coordies[1]] = sign
            return board
        else:
            print("Those coordinates were already chosen! Try again")


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