from board import Board
from piece import Piece
from player import Player
import random
import numpy as np
import pandas as pd

gameEnd = False
board = Board(9,9)
moves = [0,0]

#getting player's round and update the board
def playerRound():
    # player 1 round
    player1 = Player(Piece.BLACK)
    moves = player1.play()
    if moves[0].lower()=='q':
        return True
    board.update(int(moves[0]),int(moves[1]),player1.piece)
    #checkWin(0,0,True)
    return checkWin(int(moves[0])-1,int(moves[1])-1,True)

#check for winner
def checkWin (row, col, isPlayer):
    if isPlayer :
        piece = Piece.BLACK
    else :
        piece = Piece.WHITE
    #check row of 5
#    df = pd.DataFrame(board.boardArr)
#    blackArr = df.query(board.black)
    arr = np.array(board.boardArr)
    blackArr = np.where(arr==board.black)   
    print("Num of pieces: ",len(blackArr[1]))
    print("df: ",arr)
    print("Black Arr Col: ",blackArr[1])
    print("Black Arr Row: ",blackArr[0])
    print("Continuous Len ?:",len(blackArr[1]))

def isContinuous(arr):
    print(arr)
    prev = 0
    index = 0
    #checking continuous vertical and horizontal
    for x in arr:
        if index>0 and x-prev!=1:
            return False
        prev = x
    return True

# return a list of pieces and their continuous position (vertical, horizontal and diagonal) and an
# assigned ranking value
def evaluate(row_start, col_start, isPlayer):
    count = 0
    if isPlayer :
        piece = Piece.BLACK
    else :
        piece = Piece.WHITE
    #check up
    for x in range(col_start-1,-1,-1):
        pieceOn = board.getPiece(row_start-1,x)
        if pieceOn == piece:
            count = count+1
    if count>=5 :
        return True
    return False
# AI portion to compute a move
def computerRound():
    #simple and dumb AI
    player2 = Player(Piece.WHITE)
    valid = False
    while valid == False:
        moves[0] = random.randint(1,8)
        moves[1] = random.randint(1,8)
        valid = board.update(int(moves[0]),int(moves[1]),player2.piece)
    
while gameEnd == False:
    # player 1 round
    board.display()
    if playerRound():
        gameEnd = True
    computerRound()