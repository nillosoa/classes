

the_board = {
    "top-left": " ", "top-mid": " ", "top-right": " ",
    "mid-left": " ", "mid-mid": " ", "mid-right": " ",
    "bot-left": " ", "bot-mid": " ", "bot-right": " "
}


def print_board(board):
    print(board["top-left"] + "|" + board["top-mid"] + "|" + board["top-right"])
    print("-+-+-")
    print(board["mid-left"] + "|" + board["mid-mid"] + "|" + board["mid-right"])
    print("-+-+-")
    print(board["bot-left"] + "|" + board["bot-mid"] + "|" + board["bot-right"])
    

turn = "X"
for i in range(9):
    print_board(the_board)
    print("Turn for " + turn + ". Move on which space?")
    move = input()
    the_board[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

print_board(the_board)