import numpy as np


def get_move(game):
    for m in game.moves():
        if game.move(m).winner or game.skip().move(m).winner:
            return m
    return np.random.choice(game.moves())
