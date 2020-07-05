import numpy as np

from core.config import *
from core.game import WINNING_LINES


VALUE_GRID = np.array([[sum(map(lambda x:len(x[0])-(CONNECT-1), WINNING_LINES[(x, y)]))
                        for y in range(HEIGHT)]
                       for x in range(WIDTH)])


MAX_DEPTH = 4


# We use this as a heuristic
def position_sum(board):
    return (board * VALUE_GRID).sum()


def position_heuristic(game):
    if game.winner == 1:
        return 1000.0
    if game.winner == 2:
        return -1000.0
    return position_sum(game.board)


def get_all_lines(width, height, connect):
    lines = []
    # add these lines for each point if they lie on the board:
    #        VERT
    #        X     X SWNE
    #        X   X
    #        X X
    #        O X X X X HORI
    #          X
    #            X
    #              X NWSE

    for x in range(width):
        for y in range(height):
            # horizontal
            if x <= width - connect:
                lines.append((range(x, x+connect),
                              y))
            # vertical
            if y <= height - connect:
                lines.append((x,
                              range(y, y+connect)))
            # swne
            if x <= width - connect and y <= height - connect:
                lines.append((range(x, x + connect),
                              range(y, y + connect)))
            # nwse
            if x <= width - connect and y >= connect - 1:
                lines.append((range(x, x + connect),
                              range(y - (connect - 1), y+1)))
    return lines


ALL_LINES = get_all_lines(WIDTH, HEIGHT, CONNECT)


def lines_sum(board):
    total_score = 0.0
    for line in ALL_LINES:
        candidate = board[line]
        score = candidate.sum()
        if abs(score) and abs(score) == abs(candidate).sum():
            total_score += score
    return total_score


def lines_heuristic(game):
    if game.winner == 1:
        return 1000.0
    if game.winner == 2:
        return -1000.0
    return lines_sum(game.board)


def get_move(game, heuristic, depth=None):
    # JUST FOR SPEED
    ###
    # Be careful for seeing a 'block' before a win:
    # check for wins first:
    for m in game.moves():
        if game.move(m).winner or game.skip().move(m).winner:
            return m
    # then for blocking moves:
    for m in game.moves():
        if game.skip().move(m).winner:
            return m
    ###
    # NOW THE REAL BRAIN

    depth = depth or MAX_DEPTH

    player = -1.0 if game.turn % 2 == 1 else 1.0

    score, move = ab_negamax(game, depth, -2000.0, 2000.0, player, heuristic, top_level=True)
    # print(score)
    return move


def ab_negamax(game, depth, a, b, player, heuristic, top_level=False):
    if depth == 0 or game.winner:
        return player * heuristic(game)

    moves = game.moves()
    if len(moves) == 0:
        return player * heuristic(game)

    value = -2000.0
    best = moves[0]
    for move in moves:
        trial = -ab_negamax(game.move(move), depth-1, -b, -a, -player, heuristic) + 0.01 * depth * player
        if trial > value:
            value = trial
            best = move
        a = max(a, value)
        if a >= b:
            break

    if top_level:
        return value, best

    return value


if __name__ == '__main__':
    from core.game import Game

    g = Game().move(2).move(1).move(2).move(4).move(2).move(3).move(3)

    lines_sum(g.board)
