"""https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html"""


def check_win(board):
    result = 0
    for row in range(0, 3):
        if board[row][0] == board[row][1] and board[row][0] == board[row][2]:
            if board[row][0] == 1:
                result = 1
            elif board[row][0] == 2:
                result = 2
    for column in range(0, 3):
        if board[0][column] == board[1][column] and board[0][column] == board[2][column]:
            if board[0][column] == 1:
                result = 1
            elif board[0][column] == 2:
                result = 2
    if board[1][1] == board[0][0] and board[1][1] == board[2][2]:
        if board[1][1] == 1:
            result = 1
        elif board[1][1] == 2:
            result = 2
    elif board[1][1] == board[0][2] and board[1][1] == board[2][0]:
        if board[1][1] == 1:
            result = 1
        elif board[1][1] == 2:
            result = 2
    return result


def who_won(results):
    if results == 1:
        print("Player 1 won")
    elif results == 2:
        print("Player 2 won")
    else:
        print("It's a tie!")


game = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
winner_is_2 = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
winner_is_1 = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
winner_is_also_1 = [[0, 1, 0], [2, 1, 0], [2, 1, 1]]
no_winner = [[1, 2, 0], [2, 1, 0], [2, 1, 2]]
also_no_winner = [[1, 2, 0], [2, 1, 0], [2, 1, 0]]
who_won(check_win(game))
who_won(check_win(winner_is_2))
who_won(check_win(winner_is_1))
who_won(check_win(winner_is_also_1))
who_won(check_win(no_winner))
who_won(check_win(also_no_winner))
