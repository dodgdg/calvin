from console.utils import wait_key

from core.game import Game
from view.console_view import display
from core.brain import get_move


def main():

    game = Game()

    while True:
        winner = game.winner
        display(game, turn=game.turn, winner=winner)

        if winner:
            break

        if game.turn % 2 == 0:
            # person move
            col = wait_key(tuple(map(str, game.moves()+1)))
            game = game.move(int(col) - 1)

        else:
            # calvin move
            move = get_move(game)
            game = game.move(move)


if __name__ == '__main__':
    main()
