import unittest

from board import Board
from main import board
from piece import Piece
from player import Player

class Main_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.player1 = Player(Piece.BLACK, board)

    def test_check_horizontal_win_left_edge(self):
        # horizontal from left
        for c in range(1, 5):
            board.update(9, c, self.player1.piece)
        self.assertTrue(self.player1.check_horizontal_win(8, 4))

    def test_check_horizontal_win_right_edge(self):
        # horizontal from right
        test_board = Board(9, 9)
        for c in range(9, 5, -1):
            test_board.update(9, c, self.player1.piece)
        self.assertTrue(self.player1.check_horizontal_win(8, 4))

    def test_check_horizontal_win(self):
        # horizontal from middle
        for c in range(5, 2, -1):
            board.update(5, c, self.player1.piece)
        board.update(5, 7, self.player1.piece)
        self.assertTrue(self.player1.check_horizontal_win(4, 5))

    def test_check_vertical_win_top(self):
        # vertical from top
        for r in range(1, 5):
            board.update(r, 1, self.player1.piece)
        self.assertTrue(self.player1.check_vertical_win(4, 0))


if __name__ == '__main__':
    unittest.main()
