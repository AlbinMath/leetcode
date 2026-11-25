class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG = float('-inf')
        dp = [[[NEG] * 3 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                v = coins[i][j]
                if i == 0 and j == 0:
                    dp[0][0][0] = v
                    if v < 0:
                        dp[0][0][1] = 0
                    continue

                for k in range(3):
                    best = NEG
                    if i > 0:
                        best = max(best, dp[i - 1][j][k])
                    if j > 0:
                        best = max(best, dp[i][j - 1][k])
                    if best > NEG:
                        dp[i][j][k] = best + v

                    if v < 0 and k > 0:
                        best = NEG
                        if i > 0:
                            best = max(best, dp[i - 1][j][k - 1])
                        if j > 0:
                            best = max(best, dp[i][j - 1][k - 1])
                        if best > NEG:
                            dp[i][j][k] = max(dp[i][j][k], best)

        return max(dp[m - 1][n - 1])
