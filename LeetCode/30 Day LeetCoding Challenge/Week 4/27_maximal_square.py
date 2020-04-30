import numpy as np


class Solution:
    def maximalSquare(self, grid):
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        grid = np.array(grid)
        sub = lambda x, y, d: '0' not in grid[y:y+d, x:x+d]  # noqa: E731

        to_search = []
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    to_search.append([i, j])
        if len(to_search) == 0:
            return 0

        dim = 1
        found = True
        while found:
            found = False
            new_to_search = []
            for p in to_search:
                if p[0]+dim < height and p[1]+dim < width \
                        and sub(p[1], p[0], dim+1):
                    found = True
                    new_to_search.append(p)
            if found:
                dim += 1
            to_search = new_to_search

        return dim**2
