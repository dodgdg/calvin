import numpy as np

from core.config import *
from core.game import WINNING_LINES


VALUE_GRID = np.array([[sum(map(lambda x:len(x[0])-(CONNECT-1), WINNING_LINES[(x, y)]))
                        for y in range(HEIGHT)]
                       for x in range(WIDTH)])


MAX_DEPTH = 4  # think this should be even as our heuristic varies a lot from move to move


# We use this as a heuristic
def position_sum(board):
    return (board * VALUE_GRID).sum()


def heuristic(game):
    if game.winner == 1:
        return 1000.0
    if game.winner == 2:
        return -1000.0
    return position_sum(game.board)


def get_move(game, depth=None):
    depth = depth or MAX_DEPTH

    if game.turn % 2 == 0:
        depth -= 1  # heuristic depends on both players having same number of counters (I think)

    player = 1.0 if game.turn % 2 == 1 else -1.0

    moves = game.moves()
    scores = [(m, ab_negamax(game.move(m), depth, -2000.0, 2000.0, player))
              for m in moves]

    # print(scores)

    best = min(s[1] for s in scores)
    choices = [m for m, s in scores if s == best]
    return np.random.choice(choices)


def ab_negamax(game, depth, a, b, player):
    if depth == 0 or game.winner:
        return player * heuristic(game)

    moves = game.moves()
    if len(moves) == 0:
        return player * heuristic(game)

    value = -2000.0
    for move in moves:
        value = max(value, -ab_negamax(game.move(move), depth-1, -b, -a, -player))
        a = max(a, value)
        if a >= b:
            break
    return value


if __name__ == '__main__':
    from core.game import Game

    g = Game().move(2).move(1).move(2).move(4).move(2).move(3).move(3)

    get_move(g)
