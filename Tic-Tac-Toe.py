from os import linesep


def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):

            row_str += value
            if j != len(row) - 1:
                row_str += " | "

        print(row_str)
        if i != len(board) - 1:
            print("-----------")


def get_move(turn, board):
    while True:

        row = int(input("Row: "))
        col = int(input("col: "))

        if row < 1 or row > len(board):
            print("Invalid row,Try Again")
        elif col < 1 or col > len(board):
            print("Invalid column,Try Again")
        elif board[row - 1][col - 1] != " ":
            print("already taken,try again")
        else:
            break
    board[row - 1][col - 1] = turn


def check_win(board,turn):
    lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],

    ]
    for line in lines:
        win= True
        for pos in line:
            row, col=pos
            if board[row][col]!=turn:
                win= False
                break

        if win:
            return True

    return False


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

turn = ("x")
turn_number = 0
print_board(board)

while turn_number < 9:
    print()
    print("It is the", turn, "players turn.Please select your move.")
    get_move(turn, board)
    print_board(board)
    winner =check_win(board,turn)
    if winner:
        break

    if turn == "x":
        turn = "o"
    else:
        turn = "x"
    turn_number += 1

if turn_number==9:
    print("Tied Game")
else:
    print("The Winner was",turn)


