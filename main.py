from board import Board
from piece import Piece
from player import Player
import random

gameEnd = False
board = Board(9, 9)
moves = [0, 0]


# getting player's round and update the board
def playerRound():
    # player 1 round
    player1 = Player(Piece.BLACK, board)
    player_move = player1.play()
    if player_move[0].lower() == 'q':
        return True
    board.update(int(player_move[0]), int(player_move[1]), player1.piece)
    return player1.checkWin(int(player_move[0]) - 1, int(player_move[1]) - 1)


# AI portion to compute a move
def computerRound():
    # simple and dumb AI
    player2 = Player(Piece.WHITE)
    valid = False
    while not valid:
        moves[0] = random.randint(1, 8)
        moves[1] = random.randint(1, 8)
        valid = board.update(int(moves[0]), int(moves[1]), player2.piece)


while not gameEnd:
    # player 1 round
    board.display()
    if playerRound():
        gameEnd = True
        print('Game over Player 1 (human) has won the game')
        board.display()
        break

    computerRound()
