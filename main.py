from board import Board
from piece import Piece
from player import Player
import random

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
    return evaluate(row_start=int(moves[0]),col_start=int(moves[1]),isPlayer=True)


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