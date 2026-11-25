from typing import List

class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        cols = list(zip(*grid))
        n = len(cols)
        dp = [1] * n
        for b in range(n):
            cb = cols[b]
            for a in range(b):
                if dp[a] + 1 > dp[b]:
                    ca = cols[a]
                    if all(abs(x - y) <= limit for x, y in zip(ca, cb)):
                        dp[b] = dp[a] + 1
        return max(dp)
