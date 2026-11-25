class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        INF = float('inf')
        dp = [[INF] * n for _ in range(m)]
        dp[0][0] = 1

        def w(x, y):
            return 0 if x == 0 and y == 0 else waitCost[x][y]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                best = INF
                if i > 0:
                    best = min(best, dp[i - 1][j] + w(i - 1, j))
                if j > 0:
                    best = min(best, dp[i][j - 1] + w(i, j - 1))
                dp[i][j] = best + (i + 1) * (j + 1)

        return dp[m - 1][n - 1]
