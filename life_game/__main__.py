from life_game.display import animate
from life_game.game import LifeGame


def main():
    game = LifeGame(50, 50)
    game.randomize()
    animate(game, 10)


if __name__ == "__main__":
    main()
