import numpy as np
from life_game.game import LifeGame


def test_place():
    game = LifeGame(5, 5)
    game.place(np.array([[1, 1, 1]]), 2, 1)

    expected = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    assert np.array_equal(game.grid, expected)


def test_step():
    game = LifeGame(5, 5)
    game.place(np.array([[1, 1, 1], [1, 1, 1]]), 2, 0)

    game.step()

    expected = np.array([
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0]
        ])

    assert np.array_equal(game.grid, expected)