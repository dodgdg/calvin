from console.utils import wait_key

from core.game import Game

from view.console_view import display
# from view.debug_view import display

import brains.simple_brain as simple
import brains.tree_brain as tree


def main():

    game = Game()

    while True:
        winner = game.winner
        draw = (len(game.moves()) == 0)

        display(game, turn=game.turn, winner=winner, draw=draw)

        if winner or draw:
            break

        if game.turn % 2 == 0:
            # person move
            col = wait_key(tuple(map(str, game.moves()+1)))
            game = game.move(int(col) - 1)
            # move = tree.get_move(game, tree.position_heuristic, depth=4)
            # game = game.move(move)

        else:
            # calvin move
            move = tree.get_move(game, tree.lines_heuristic, depth=4)
            game = game.move(move)


if __name__ == '__main__':
    main()
