from console.utils import wait_key

from core.game import Game

from view.console_view import display
# from view.debug_view import display

# from brains.simple_brain import get_move
from brains.tree_brain import get_move


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
            # move = get_move(game, depth=6)
            # game = game.move(move)

        else:
            # calvin move

            # bit of speed optimisation:
            if game.turn < 8:
                depth = 4  # opening
            elif len(game.moves()) < 5:  # endgame
                depth = 10
            else:
                depth = 6  # middlegame
            move = get_move(game, depth=depth)
            game = game.move(move)


if __name__ == '__main__':
    main()
