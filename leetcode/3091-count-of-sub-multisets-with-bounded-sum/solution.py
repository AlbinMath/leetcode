from typing import List
from collections import Counter

class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7
        cnt = Counter(nums)
        zeros = cnt.pop(0, 0)

        dp = [0] * (r + 1)
        dp[0] = 1

        for v, c in cnt.items():
            new = dp[:]                      # j = 0 term
            for s in range(v, r + 1):
                val = new[s - v] + dp[s]
                if s - (c + 1) * v >= 0:
                    val -= dp[s - (c + 1) * v]
                new[s] = val % MOD
            dp = new

        # careful: new[s] above must equal sum_{j=0..c} dp[s - j*v]
        return sum(dp[l:r + 1]) % MOD * (zeros + 1) % MOD
