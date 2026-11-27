from typing import List

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        INF = float('inf')
        dp = [1, 0, 1]
        for i in range(1, len(obstacles)):
            o = obstacles[i]
            if o:
                dp[o - 1] = INF
            best = min(dp)
            for l in range(3):
                if l != o - 1:
                    dp[l] = min(dp[l], best + 1)
        return min(dp)
