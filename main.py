from board import Board
from piece import Piece
from player import Player
import random

gameEnd = False
board = Board(9, 9)
moves = [0, 0]


#getting player's round and update the board
def playerRound():
    # player 1 round
    player1 = Player(Piece.BLACK)
    moves = player1.play()
    if moves[0].lower() == 'q':
        return True
    board.update(int(moves[0]), int(moves[1]), player1.piece)
    return checkWin(int(moves[0]) - 1, int(moves[1]) - 1, True)


#check for winner
def checkWin(row, col, isPlayer):
    if isPlayer:
        piece = Piece.BLACK
    else:
        piece = Piece.WHITE

    if (row >= 8 and col >= 8) or (row <= 0 and col <= 0):
        # only check backward diagonal, horizontal and vertical
        return check_horizontal_win(row, col, piece) or check_vertical_win(row, col, piece) or check_diagonal_b_win(row,
                                                                                                                    col,
                                                                                                                    piece)
    elif (row <= 0 and col >= 8) or (row >= 8 and col <= 0):
        # only check foreward diagonal, horizontal and vertical
        return check_horizontal_win(row, col, piece) or check_vertical_win(row, col, piece) or check_diagonal_f_win(row,
                                                                                                                    col,
                                                                                                                    piece)
    else:
        return check_horizontal_win(row, col, piece) or check_vertical_win(row, col, piece) or check_diagonal_f_win(row,
                                                                                                                    col,
                                                                                                                    piece) or check_diagonal_b_win(
            row, col, piece)


# checking \ diagonal backward moves
def check_diagonal_b_win(r, c, piece):
    leftcnt = 0
    rightcnt = 0
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
        #top left corner
        start_r = r + 1
        start_c = c + 1
        isTopLeftCorner = True
    # count left up
    if isTopLeftCorner == False:
        leftcnt = countDF_Piece(start_r - 1, -1, start_c - 1, -1, piece)
        print('leftcnt: ', leftcnt)
    else:
        leftcnt = 0
    # count right down
    if isBottomRightCorner == False:
        rightcnt = countDF_Piece(start_r + 1, board.rows, start_c + 1, board.cols, piece)
        print('rightcnt: ', rightcnt)
    else:
        rightcnt = 0
    totalcnt = totalcnt + leftcnt + rightcnt
    print('total cnt: ', totalcnt)
    if totalcnt == 5:
        return True

    return False


# checking / diagonal forward moves 
def check_diagonal_f_win(r, c, piece):
    leftcnt = 0
    rightcnt = 0
    totalcnt = 1
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
        #top right corner
        start_r = r + 1
        start_c = c - 1
        isTopRightCorner = True
    # count left down
    if isBottomLeftCorner == False:
        leftcnt = countDF_Piece(start_r + 1, board.rows, start_c - 1, -1, piece)
    else:
        leftcnt = 0
    # count right up
    if isTopRightCorner == False:
        rightcnt = countDF_Piece(start_r - 1, -1, start_c + 1, board.cols, piece)
    else:
        rightcnt = 0
    totalcnt = totalcnt + leftcnt + rightcnt
    if totalcnt == 5:
        return True

    return False


#check for win vertically
def check_vertical_win(r, c, piece):
    upcnt = 0
    downcnt = 0
    totalcnt = 1
    if r > 0:
        start = r - 1
    elif r <= 0:
        #top row of the board
        start = max(0, r)
    #count up
    upcnt = countV_Piece(c, start, -1, piece)
    if r < board.rows - 1:
        downcnt = countV_Piece(c, r + 1, board.rows, piece)
    else:
        #bottom column of the board
        downcnt = 0
    totalcnt = totalcnt + upcnt + downcnt
    if totalcnt == 5:
        return True

    return False


# check for win horizontally
def check_horizontal_win(r, c, piece):
    total_count = 1
    start = 0
    if c > 0:
        start = c - 1
    elif c <= 0:
        #first column of the board
        start = max(0, c)
    # count left
    left_count = countH_Piece(r, start, -1, piece)
    if c < board.cols - 1:
        right_count = countH_Piece(r, c + 1, board.cols, piece)
    else:
        #last column of the board
        right_count = 0
    total_count = total_count + left_count + right_count
    if total_count == 5:
        return True
    return False


def countDF_Piece(start_r, end_r, start_c, end_c, piece):
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
        if board.getPiece(r, start_c) == piece:
            cnt = cnt + 1
        else:
            break
        start_c = start_c + c_incr
    return cnt


def countV_Piece(c, start, end, piece):
    cnt = 0
    increment = 1
    if start > end:
        increment = -1
    for r in range(start, end, increment):
        if board.getPiece(r, c) == piece:
            cnt = cnt + 1
        else:
            break
    return cnt


def countH_Piece(r, start, end, piece):
    cnt = 0
    increment = 1
    if start > end:
        increment = -1
    for c in range(start, end, increment):
        if board.getPiece(r, c) == piece:
            cnt = cnt + 1
        else:
            break
    return cnt


# AI portion to compute a move
def computerRound():
    #simple and dumb AI
    player2 = Player(Piece.WHITE)
    valid = False
    while valid == False:
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
