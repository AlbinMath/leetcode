class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        px = [[0] * n for _ in range(m)]
        py = [[0] * n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                x = 1 if grid[i][j] == 'X' else 0
                y = 1 if grid[i][j] == 'Y' else 0
                if i > 0:
                    x += px[i - 1][j]
                    y += py[i - 1][j]
                if j > 0:
                    x += px[i][j - 1]
                    y += py[i][j - 1]
                if i > 0 and j > 0:
                    x -= px[i - 1][j - 1]
                    y -= py[i - 1][j - 1]
                px[i][j], py[i][j] = x, y
                if x > 0 and x == y:
                    res += 1

        return res
