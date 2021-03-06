import numpy as np


def get_move(game):
    # Be careful for seeing a 'block' before a win:
    # check for wins first:
    for m in game.moves():
        if game.move(m).winner:
            return m
    # then for blocking moves:
    for m in game.moves():
        if game.skip().move(m).winner:
            return m
    return np.random.choice(game.moves())
