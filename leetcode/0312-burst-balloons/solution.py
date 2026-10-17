from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        a = [1] + nums + [1]
        m = len(a)
        dp = [[0] * m for _ in range(m)]
        for gap in range(2, m):
            for i in range(m - gap):
                j = i + gap
                best = 0
                for k in range(i + 1, j):
                    v = dp[i][k] + dp[k][j] + a[i] * a[k] * a[j]
                    if v > best:
                        best = v
                dp[i][j] = best
        return dp[0][m - 1]
