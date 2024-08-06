# Board Class to store the state of the game and also to display
from piece import Piece
import os
class Board:
    def __init__(self,rows,cols) :
        self.space = '  '
        self.blank = ' - '
        self.black = ' x '
        self.white = ' o '
        self.rows = rows
        self.cols = cols
        self.boardArr = [[ self.blank  for i in range(cols)] for j in range(rows)]

    def getPiece(self,row,col):
        if self.isWithinRange(row,col)==False:
            print('Error')
            return None
        if self.boardArr[row][col] == self.black:
            return Piece.BLACK
        elif self.boardArr[row][col] == self.white:
            return Piece.WHITE
        else:
            return Piece.BLANK

        
        
    def display(self):
        os.system('cls')
        self.populateHeader()
        data = ''
        for r in range(self.rows):
            data = data + str(r+1)
            for c in range(self.cols):
                data = data + self.boardArr[r][c]
            data = data + '\n'
        print(data)

    def populateHeader(self):
        content =  self.space
        for c in range(self.cols):
            content = content + str(c+1) + self.space
        print(content)

    def update(self,rowIndx,colIndx,piece):
        if self.isWithinRange(rowIndx,colIndx)==False:
            print('Error')
            return False
        if self.isEmpty(rowIndx,colIndx)==False:
            print('Invalid move')
            return False
        if piece == Piece.BLACK:
            self.boardArr[rowIndx-1][colIndx-1]=self.black 
        elif piece == Piece.WHITE:
            self.boardArr[rowIndx-1][colIndx-1]=self.white
    
    def isWithinRange(self,rowIndx,colIndx):
        if rowIndx>self.rows+1 or colIndx>self.cols+1 or rowIndx==0 or colIndx==0:
            return False
        else:
            return True
    
    def isEmpty(self,rowIndx, colIndx):
        if self.isWithinRange(rowIndx,colIndx)==False:
            print('Error')
            return None
        if self.boardArr[rowIndx-1][colIndx-1]==self.blank:
            return True
        else:
            return False
