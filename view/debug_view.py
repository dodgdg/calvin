

def disp(num):
    if num > 0:
        return 'X'
    if num < 0:
        return 'O'
    return ' '


def display(board, turn, winner, draw):
    print('===')
    print(f'winner={winner}')
    print(f'draw={draw}')
    print(f'turn={turn} ({"player" if turn % 2 == 0 else "calvin"})')
    print()
    for row in board.board.T[::-1]:
        print(' '.join(map(disp, row)))
    print(' '.join(map(str, range(1, board.width + 1))))
