class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        def count(g):
            m, n = len(g), len(g[0])
            dp = [[0] * n for _ in range(m)]
            res = 0
            for i in range(m):
                for j in range(n):
                    if g[i][j] == 0:
                        continue
                    if i == 0 or j == 0 or j == n - 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + 1
                    res += dp[i][j] - 1
            return res

        return count(grid) + count(grid[::-1])
