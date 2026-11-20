from typing import List

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        if grid[0][0] != 0:
            return False

        pos = [None] * (n * n)
        for r in range(n):
            for c in range(n):
                pos[grid[r][c]] = (r, c)

        for v in range(n * n - 1):
            r1, c1 = pos[v]
            r2, c2 = pos[v + 1]
            if abs(r1 - r2) * abs(c1 - c2) != 2:
                return False
        return True
