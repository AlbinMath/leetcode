class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rows = 0
        for row in grid:
            for j in range(n // 2):
                if row[j] != row[n - 1 - j]:
                    rows += 1

        cols = 0
        for i in range(m // 2):
            top, bot = grid[i], grid[m - 1 - i]
            for j in range(n):
                if top[j] != bot[j]:
                    cols += 1

        return min(rows, cols)
