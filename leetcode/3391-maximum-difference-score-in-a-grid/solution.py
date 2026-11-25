class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        mn = [[INF] * n for _ in range(m)]
        res = -INF

        for i in range(m):
            for j in range(n):
                prev = INF
                if i > 0:
                    prev = min(prev, mn[i - 1][j])
                if j > 0:
                    prev = min(prev, mn[i][j - 1])

                if prev != INF:
                    res = max(res, grid[i][j] - prev)

                mn[i][j] = min(grid[i][j], prev)

        return res
