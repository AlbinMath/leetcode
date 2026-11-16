from typing import List

class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        n = len(strength)
        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] == INF:
                continue
            x = 1 + k * bin(mask).count("1")
            for j in range(n):
                if mask >> j & 1:
                    continue
                t = -(-strength[j] // x)  # ceil division
                nm = mask | (1 << j)
                if dp[mask] + t < dp[nm]:
                    dp[nm] = dp[mask] + t
        return dp[(1 << n) - 1]
