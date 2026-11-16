from typing import List
from math import gcd

class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        m = len(target)
        full = (1 << m) - 1

        lcm = [1] * (1 << m)
        for mask in range(1, 1 << m):
            low = (mask & -mask).bit_length() - 1
            prev = mask & (mask - 1)
            l = lcm[prev]
            t = target[low]
            lcm[mask] = l * t // gcd(l, t)

        INF = float('inf')
        dp = [INF] * (1 << m)
        dp[0] = 0

        for x in nums:
            cost = [0] * (1 << m)
            for s in range(1, 1 << m):
                cost[s] = (-x) % lcm[s]
            new = dp[:]
            for mask in range(1 << m):
                if dp[mask] == INF:
                    continue
                rest = full ^ mask
                sub = rest
                while sub:
                    nm = mask | sub
                    v = dp[mask] + cost[sub]
                    if v < new[nm]:
                        new[nm] = v
                    sub = (sub - 1) & rest
            dp = new

        return dp[full]
