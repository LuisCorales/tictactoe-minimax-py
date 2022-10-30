from game import *


def aiMove():
    bestScore = -1000
    move = 0
    for key in board.keys():
        if board[key] == " ":
            board[key] = botMark
            score = minimax(board, 0, False)
            board[key] = " "
            if score > bestScore:
                bestScore = score
                move = key
    insertMark(botMark, move)
    return


def minimax(board, depth, isMaximizing):
    if checkWinner(botMark):
        return 1
    elif checkWinner(playerMark):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -1
        for key in board.keys():
            if board[key] == " ":
                board[key] = botMark
                score = minimax(board, depth + 1, False)
                board[key] = " "
                if score > bestScore:
                    bestScore = score
        return bestScore

    else:
        bestScore = 1
        for key in board.keys():
            if board[key] == " ":
                board[key] = playerMark
                score = minimax(board, depth + 1, True)
                board[key] = " "
                if score < bestScore:
                    bestScore = score
        return bestScore
