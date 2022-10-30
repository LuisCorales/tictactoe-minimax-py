board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")


def isPositionFree(pos):
    if board[pos] == " ":
        return True
    else:
        return False


def insertMark(mark, pos):
    if isPositionFree(pos):
        board[pos] = mark
        return
    else:
        print("The position is not free")
        return


printBoard(board)
