from typing import List

class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            dp[h][w] = p

        for h in range(1, m + 1):
            for w in range(1, n + 1):
                best = dp[h][w]
                for i in range(1, h // 2 + 1):
                    v = dp[i][w] + dp[h - i][w]
                    if v > best:
                        best = v
                for j in range(1, w // 2 + 1):
                    v = dp[h][j] + dp[h][w - j]
                    if v > best:
                        best = v
                dp[h][w] = best
        return dp[m][n]
