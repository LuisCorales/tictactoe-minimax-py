board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")


def checkWinner(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] == mark:
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        # If there is an empty space, not draw
        if board[key] == " ":
            return False
    return True


def playerMove():
    while True:
        pos = input("Enter the position for " + playerMark + ": ")
        while not pos.isdigit():
            pos = input("Enter valid position for " + playerMark + ": ")
        if insertMark(playerMark, int(pos)):
            return


def isPositionFree(pos):
    if board[pos] == " ":
        return True
    else:
        return False


def insertMark(mark, pos):
    if isPositionFree(pos):
        board[pos] = mark
        return True
    else:
        print("The position is not free")
        return False


botMark = "O"
playerMark = "X"
