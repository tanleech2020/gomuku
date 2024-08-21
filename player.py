from piece import Piece

class Player:
    def __init__(self, piece):
        self.piece = piece
    
    def play(self):
        moves = input('Enter your move (eg 78 is row 7 and column 8) or q(Q) to quit:')
        return moves




