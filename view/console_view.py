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


def draw_msg():
    return fg.lightgreen('Draw!!!')


def turn_msg(turn):
    if turn % 2 == 0:
        return fg.lightblue('Your turn...')
    if turn % 2 == 1:
        return fg.red('Calvin\'s turn...')


def display(game, winner, draw=False):
    clear_screen()

    if winner:
        print(winner_msg(winner))
    elif draw:
        print(draw_msg())
    else:
        print(turn_msg(game.turn))

    print(fg.lightpurple(' '.join(map(str, range(1, game.width + 1)))))
    print(fg.lightgreen(bg.lightgreen('  ') * game.width))

    for row in game.board.T[::-1]:
        print(' '.join((map(color, row))))

    print(fg.lightgreen(bg.lightgreen('  ') * game.width))
    print(fg.lightpurple(' '.join(map(str, range(1, game.width + 1)))))
