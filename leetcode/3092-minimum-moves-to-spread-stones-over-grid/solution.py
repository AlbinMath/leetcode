from typing import List
from itertools import permutations

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        sources = []  # one entry per extra stone
        targets = []  # one entry per empty cell
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    targets.append((i, j))
                elif grid[i][j] > 1:
                    sources.extend([(i, j)] * (grid[i][j] - 1))

        if not targets:
            return 0

        best = float('inf')
        for perm in permutations(targets):
            cost = sum(abs(a[0] - b[0]) + abs(a[1] - b[1])
                       for a, b in zip(sources, perm))
            best = min(best, cost)
        return best
