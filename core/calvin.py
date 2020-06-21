from console.utils import wait_key

from core.board import Board
from view.console_view import display


def main():

    board = Board()

    while True:
        winner = board.winner()
        display(board, turn=board.turn, winner=winner)
        col = wait_key(tuple(map(str, range(1, board.width+1))))

        try:
            board = board.move(int(col) - 1)
        except:
            pass


if __name__ == '__main__':
    main()

# import os
#
#
# def make_counter(num):
#     if num == 1.0:
#         return 'O'
#     if num == -1.0:
#         return 'X'
#     return ' '
#
#
# def display(board):
#     os.system('clear')
#
#     print('Calvin')
#     print()
#
#     for row in board.board.T:
#         print(' '.join((map(make_counter, row))))
#
#     print('_' * board.width * 2)
#     print(' '.join(map(str, range(1, board.width + 1))))
