import numpy as np


def get_move(game):
    for m in game.moves():
        if game.move(m).winner == 2:
            return m
    return np.random.choice(game.moves())
