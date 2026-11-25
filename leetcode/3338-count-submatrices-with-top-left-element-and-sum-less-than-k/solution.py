class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        P = [[0] * n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if i > 0:
                    v += P[i - 1][j]
                if j > 0:
                    v += P[i][j - 1]
                if i > 0 and j > 0:
                    v -= P[i - 1][j - 1]
                P[i][j] = v
                if v <= k:
                    res += 1

        return res
