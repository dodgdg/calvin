import numpy as np


def check_vertical_wins(arr, connect):
    cumulative = arr.cumsum(axis=1)
    candidates = np.hstack((cumulative[:, connect - 1].reshape(-1, 1),
                            (cumulative[:, connect:] - cumulative[:, :-connect])))
    if connect in candidates:
        return 1
    if -connect in candidates:
        return 2


class Board:
    def __init__(self, board=None, turn=0, connect=4):
        self.connect = connect
        self.board = board if board is not None else np.zeros([7, 6])
        self.width, self.height = self.board.shape
        self.turn = turn

    def move(self, col):
        height = int(np.abs(self.board[col]).sum())
        if height >= self.height:
            raise IndexError('Not enough space in board')
        ret = self.board.copy()
        ret[col, height] = 1 - (self.turn % 2) * 2
        return Board(board=ret,
                     turn=self.turn + 1,
                     connect=self.connect)

    def winner(self):
        # vertical, horizontal, NE-diagonal, NW-diagonal
        print()
        return check_vertical_wins(self.board, self.connect) \
               or check_vertical_wins(self.board.T, self.connect)


if __name__ == '__main__':
    b = Board().move(1).move(0).move(1).move(3).move(1).move(4).move(1).move(5).move(6).move(3).move(4).move(6).move(5)
    b.winner()