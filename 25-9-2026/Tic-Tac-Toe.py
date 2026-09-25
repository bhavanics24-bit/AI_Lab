
import random

board = [" "] * 9
wins = [(0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)]

def show():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def win(p):
    return any(board[a] == board[b] == board[c] == p
               for a,b,c in wins)

def bot():
    # Win or block
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if win("O"):
                return
            board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if win("X"):
                board[i] = "O"
                return
            board[i] = " "

    # Center
    if board[4] == " ":
        board[4] = "O"
        return

    # Corner
    for i in [0,2,6,8]:
        if board[i] == " ":
            board[i] = "O"
            return

    # Random
    empty = [i for i in range(9) if board[i] == " "]
    board[random.choice(empty)] = "O"


while True:
    show()

    p = int(input("Enter position (1-9): ")) - 1

    if p < 0 or p > 8 or board[p] != " ":
        print("Invalid position")
        continue

    board[p] = "X"

    if win("X"):
        show()
        print("You Win!")
        break

    if " " not in board:
        print("Draw!")
        break

    bot()

    if win("O"):
        show()
        print("Bot Wins!")
        break

    if " " not in board:
        print("Draw!")
        break
