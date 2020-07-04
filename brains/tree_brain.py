import numpy as np

from core.game import WINNING_LINES


VALUE_GRID = np.array([[sum(map(lambda x:len(x[0])-3, WINNING_LINES[(x, y)]))
                        for y in range(6)]
                       for x in range(7)])


MAX_DEPTH = 4  # think this should be odd as our heuristic varies a lot from move to move


# We use this as a heuristic
def position_sum(board):
    return (board * VALUE_GRID).sum()


def heuristic(game):
    if game.winner == 1:
        return 1000.0
    if game.winner == 2:
        return -1000.0
    return position_sum(game.board)


def get_move(game):
    moves = game.moves()
    scores = [(m, ab_negamax(game.move(m), MAX_DEPTH, -2000.0, 2000.0, 1.0))
              for m in moves]

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
