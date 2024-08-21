from piece import Piece


class Player:
    def __init__(self, piece, board):
        self.piece = piece
        self.board = board

    def play(self):
        moves = input('Enter your move (eg 78 is row 7 and column 8) or q(Q) to quit:')
        return moves

    # check for winner
    def checkWin(self, row, col):

        if (row >= 8 and col >= 8) or (row <= 0 and col <= 0):
            # only check backward diagonal, horizontal and vertical
            return (self.check_horizontal_win(row, col) or self.check_vertical_win(row, col)
                    or self.check_diagonal_b_win(row, col))
        elif (row <= 0 and col >= 8) or (row >= 8 and col <= 0):
            # only check forward diagonal, horizontal and vertical
            return (self.check_horizontal_win(row, col) or self.check_vertical_win(row, col)
                    or self.check_diagonal_f_win(row,
                                                 col))
        else:
            return (self.check_horizontal_win(row, col) or self.check_vertical_win(row, col)
                    or self.check_diagonal_f_win(row,
                                                 col) or self.check_diagonal_b_win(row, col))

    # checking \ diagonal backward moves
    def check_diagonal_b_win(self, r, c):
        totalcnt = 1
        isTopLeftCorner = False
        isBottomRightCorner = False
        start_r = r
        start_c = c
        if r >= 8 and c >= 8:
            # bottom right corner
            start_r = r - 1
            start_c = c - 1
            isBottomRightCorner = True
        elif r <= 0 and c <= 0:
            # top left corner
            start_r = r + 1
            start_c = c + 1
            isTopLeftCorner = True
        # count left up
        if not isTopLeftCorner:
            left_count = self.countDF_Piece(start_r - 1, -1, start_c - 1, -1)
        #        print('left_count: ', left_count)
        else:
            left_count = 0
        # count right down
        if not isBottomRightCorner:
            right_count = self.countDF_Piece(start_r + 1, self.board.rows, start_c + 1, self.board.cols)
        #        print('right_count: ', right_count)
        else:
            right_count = 0
        totalcnt = totalcnt + left_count + right_count
        #    print('total cnt: ', totalcnt)
        if totalcnt == 5:
            return True

        return False

    # checking / diagonal forward moves
    def check_diagonal_f_win(self, r, c):
        total_count = 1
        isTopRightCorner = False
        isBottomLeftCorner = False
        start_r = r
        start_c = c
        if r >= 8 and c <= 0:
            # bottom left corner
            start_r = r - 1
            start_c = c + 1
            isBottomLeftCorner = True
        elif r <= 0 and c >= 8:
            # top right corner
            start_r = r + 1
            start_c = c - 1
            isTopRightCorner = True
        # count left down
        if not isBottomLeftCorner:
            left_count = self.countDF_Piece(start_r + 1, self.board.rows, start_c - 1, -1)
        else:
            left_count = 0
        # count right up
        if not isTopRightCorner:
            right_count = self.countDF_Piece(start_r - 1, -1, start_c + 1, self.board.cols)
        else:
            right_count = 0
        total_count = total_count + left_count + right_count
        if total_count == 5:
            return True

        return False

    # check for win vertically
    def check_vertical_win(self, r, c):
        total_count = 1
        start = 0
        if r > 0:
            start = r - 1
        elif r <= 0:
            # top row of the board
            start = max(0, r)
        # count up
        up_count = self.count_piece_straight(None, c, start, -1)  # countV_Piece(c, start, -1, piece)
        if r < self.board.rows - 1:
            down_count = self.count_piece_straight(None, c, r + 1, self.board.rows)  # countV_Piece(c, r + 1, board.rows, piece)
        else:
            # bottom column of the board
            down_count = 0
        total_count = total_count + up_count + down_count
        if total_count == 5:
            return True

        return False

    # check for win horizontally
    def check_horizontal_win(self, r, c):
        total_count = 1
        start = 0
        if c > 0:
            start = c - 1
        elif c <= 0:
            # first column of the board
            start = max(0, c)
        # count left
        left_count = self.count_piece_straight(r, None, start, -1)
        if c < self.board.cols - 1:
            right_count = self.count_piece_straight(r, None, c + 1, self.board.cols)
        else:
            # last column of the board
            right_count = 0
        total_count = total_count + left_count + right_count
        if total_count == 5:
            return True
        return False

    def countDF_Piece(self, start_r, end_r, start_c, end_c):
        cnt = 0
        if end_r > start_r and end_c < start_c:
            r_incr = 1
            c_incr = -1
        elif end_r < start_r and end_c < start_c:
            r_incr = -1
            c_incr = -1
        elif end_r > start_r and end_c > start_c:
            r_incr = 1
            c_incr = 1
        else:
            r_incr = -1
            c_incr = 1

        for r in range(start_r, end_r, r_incr):
            if self.board.getPiece(r, start_c) == self.piece:
                cnt = cnt + 1
            else:
                break
            start_c = start_c + c_incr
        return cnt

    def count_piece_straight(self, r, c, start, end):
        cnt = 0
        increment = 1
        if start > end:
            increment = -1

        if r is None and c is not None:
            # count vertical
            for r in range(start, end, increment):
                if self.board.getPiece(r, c) == self.piece:
                    cnt = cnt + 1
                else:
                    break
        elif r is not None and c is None:
            # count horizontal
            for c in range(start, end, increment):
                if self.board.getPiece(r, c) == self.piece:
                    cnt = cnt + 1
                else:
                    break
        return cnt
