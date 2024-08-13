from board import Board
from piece import Piece
from player import Player
import random
import numpy as np
import pandas as pd
import collections

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
    isWin = checkWin(int(moves[0])-1,int(moves[1])-1,True)
    print(isWin)
    return isWin

#check for winner
def checkWin (row, col, isPlayer):
    if isPlayer :
        piece = Piece.BLACK
    else :
        piece = Piece.WHITE
    return check_horizontal_win(row,col,piece)

def check_horizontal_win(r,c,piece):
    hStart = max(0,c-4)
    

    return False

def countH_Piece(r,start,end, piece):
    cnt = 0
    for c in range(start,end):
        print('start',start)
        print('end',end)
        if board.getPiece(r,c)==piece:
            cnt = cnt + 1 
    print(cnt)
    return cnt

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