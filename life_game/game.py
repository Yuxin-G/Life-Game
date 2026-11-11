"""
This module contains the class of LifeGame
"""
import numpy as np


class LifeGame:
    def __init__(self, rows, cols):
        self.grid = np.zeros((rows, cols), dtype=int)

    def randomize(self, density=0.3):
        self.grid = np.random.binomial(1, density, size=self.grid.shape)

    def place(self, pattern, row, col):
        r, c = pattern.shape
        self.grid[row:row + r, col:col + c] = pattern

    def count_neighbors(self):
        total = np.zeros(self.grid.shape, dtype=int)
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dy == 0 and dx == 0:
                    continue
                total += np.roll(self.grid, (dy, dx), axis=(0, 1))
        return total

    def step(self):
        counts = self.count_neighbors()
        # rows, cols = counts.shape
        # for x in range(rows):
        #     for y in range(cols):
        #         if counts[x][y] == 3:
        #             self.grid[x][y] = 1
        #         else:
        #             if counts[x][y] != 2:
        #                 self.grid[x][y] = 0
        self.grid = ((counts == 3) | ((self.grid == 1) & (counts == 2))).astype(int)
