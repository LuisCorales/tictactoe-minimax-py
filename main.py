from game import *
from minimax import *

global firstComputerMove
firstComputerMove = True

posBoard = {1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6',
            7: '7', 8: '8', 9: '9'}

printBoard(posBoard)

while True:
    aiMove()
    printBoard(board)
    if checkWinner(playerMark):
        print("PLAYER WINS!")
        break
    elif checkWinner(botMark):
        print("BOT WINS!")
        break
    elif checkDraw():
        print("DRAW!")
        break
    playerMove()
    printBoard(board)
