from math import isqrt

class Solution:
    def longestSquareStreak(self, nums):
        dp = {}
        best = 0
        for v in sorted(set(nums)):
            r = isqrt(v)
            if r * r == v and r in dp:
                dp[v] = dp[r] + 1
                best = max(best, dp[v])
            else:
                dp[v] = 1
        return best if best >= 2 else -1
