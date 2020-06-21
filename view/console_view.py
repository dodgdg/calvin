import os

from console import fg, bg
from console.screen import sc
from console.utils import set_title, clear_screen


def color(num):
    if num == 1.0:
        return fg.lightblue('O')
    if num == -1.0:
        return fg.red('O')
    return ' '


def winner_msg(winner):
    if winner == 1:
        return fg.lightblue('You won!!!')
    if winner == 2:
        return fg.red('Calvin won!!!')


def turn_msg(turn):
    if turn % 2 == 0:
        return fg.lightblue('Your turn...')
    if turn % 2 == 1:
        return fg.red('Calvin\'s turn...')


def display(board, turn, winner):
    clear_screen()

    if winner:
        print(winner_msg(winner))
    else:
        print(turn_msg(turn))

    print(fg.lightpurple(' '.join(map(str, range(1, board.width + 1)))))
    print(fg.lightgreen(bg.lightgreen('  ') * board.width))

    for row in board.board.T[::-1]:
        print(' '.join((map(color, row))))

    print(fg.lightgreen(bg.lightgreen('  ') * board.width))
    print(fg.lightpurple(' '.join(map(str, range(1, board.width + 1)))))
