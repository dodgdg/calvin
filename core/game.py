import numpy as np


def get_winning_lines(width, height, connect):
    lines_dic = {}

    def clip(ran_x, ran_y):
        clipped = [(x, y) for x, y in zip(ran_x, ran_y)
                   if 0 <= x < width
                   and 0 <= y < height]
        if len(clipped) >= connect:
            return tuple(zip(*clipped))

    for x in range(width):
        for y in range(height):
            # horizontal
            hori = clip(range(x-(connect-1), x+connect),
                        (2*connect-1)*[y])
            # vertical - only need to check below
            vert = clip((2*connect-1)*[x],
                        range(y-(connect-1), y+1))
            # SW to NE
            swne = clip(range(x-(connect-1), x+connect),
                        range(y-(connect-1), y+connect))
            # NW to SE
            nwse = clip(range(x-(connect-1), x+connect),
                        range(y+(connect-1), y-connect, -1))
            lines_dic[(x, y)] = [line for line in [hori, vert, swne, nwse] if line is not None]
    return lines_dic


WINNING_LINES = get_winning_lines(7, 6, 4)


def winning(board, connect, last_move):
    # Most recently placed piece must be a part of the winning line - so just check around this point
    for line in WINNING_LINES[last_move]:
        cumulative = board[line].cumsum()
        candidates = list(cumulative[connect:] - cumulative[:-connect]) + [cumulative[connect-1]]
        if connect in candidates:
            return 1
        if -connect in candidates:
            return 2


class Game:
    def __init__(self, board=None, turn=0, connect=4, winner=0):
        self.board = board if board is not None else np.zeros([7, 6])
        self.width, self.height = self.board.shape
        self.turn = turn
        self.connect = connect
        self.winner = winner

        self.winning_lines = get_winning_lines(self.width, self.height, self.connect)

    def moves(self):
        return np.array(range(self.width))[self.board.prod(axis=1) == 0]

    def move(self, col):
        height = int(np.abs(self.board[col]).sum())
        if height >= self.height:
            raise IndexError('Not enough space in board')
        ret = self.board.copy()
        ret[col, height] = 1 - (self.turn % 2) * 2
        return Game(board=ret,
                     turn=self.turn + 1,
                     connect=self.connect,
                     winner=self.winner or winning(ret, self.connect, (col, height)))


if __name__ == '__main__':
    b = Game().move(1).move(6).move(2).move(6).move(3).move(6).move(4)
    b.moves()

