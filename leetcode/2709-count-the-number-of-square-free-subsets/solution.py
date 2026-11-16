from typing import List
from collections import Counter

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        def get_mask(v: int) -> int:
            m = 0
            for i, p in enumerate(primes):
                if v % p == 0:
                    v //= p
                    if v % p == 0:
                        return -1  # p squared divides it
                    m |= 1 << i
            return m

        cnt = Counter(nums)
        dp = [0] * 1024
        dp[0] = 1

        for v in range(2, 31):
            c = cnt.get(v, 0)
            if c == 0:
                continue
            m = get_mask(v)
            if m < 0:
                continue
            for mask in range(1023, -1, -1):
                if mask & m == 0 and dp[mask]:
                    dp[mask | m] = (dp[mask | m] + dp[mask] * c) % MOD

        total = sum(dp) % MOD
        total = total * pow(2, cnt.get(1, 0), MOD) % MOD
        return (total - 1) % MOD
