from typing import List

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        by_end = [[] for _ in range(n + 1)]
        for s, e, t in rides:
            by_end[e].append((s, e - s + t))

        dp = [0] * (n + 1)
        for p in range(1, n + 1):
            dp[p] = dp[p - 1]
            for s, earn in by_end[p]:
                dp[p] = max(dp[p], dp[s] + earn)

        return dp[n]
