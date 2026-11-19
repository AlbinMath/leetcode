from typing import List
from collections import Counter

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        M = 1 << 10
        INF = float('inf')
        dp = [INF] * M
        dp[0] = 0

        for j in range(k):
            cnt = Counter(nums[j::k])
            size = sum(cnt.values())
            best = min(dp)
            new_dp = [best + size] * M   # change whole class to any value
            for x in range(M):
                if dp[x] == INF:
                    continue
                for v, f in cnt.items():
                    t = x ^ v
                    c = dp[x] + size - f
                    if c < new_dp[t]:
                        new_dp[t] = c
            dp = new_dp

        return dp[0]
