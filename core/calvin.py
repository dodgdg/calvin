from console.utils import wait_key

from core.game import Game
from view.console_view import display
from core.brain import get_move


def main():

    game = Game()

    while True:
        winner = game.winner
        display(game, turn=game.turn, winner=winner)

        if winner:
            break

        if game.turn % 2 == 0:
            # person move
            col = wait_key(tuple(map(str, game.moves()+1)))
            game = game.move(int(col) - 1)

        else:
            # calvin move
            move = get_move(game)
            game = game.move(move)


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
