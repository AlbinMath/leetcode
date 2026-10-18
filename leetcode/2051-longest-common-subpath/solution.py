import random
from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        MOD = (1 << 61) - 1
        BASE = random.randrange(10**6, MOD - 1)

        def common(L: int) -> bool:
            top = pow(BASE, L, MOD)          # BASE^L, to remove the outgoing element
            cur = None
            for p in paths:
                if len(p) < L:
                    return False
                h = 0
                for i in range(L):
                    h = (h * BASE + p[i] + 1) % MOD
                hashes = {h}
                for i in range(L, len(p)):
                    h = (h * BASE + p[i] + 1 - (p[i - L] + 1) * top) % MOD
                    hashes.add(h)
                cur = hashes if cur is None else (cur & hashes)
                if not cur:
                    return False
            return True

        lo, hi = 0, min(len(p) for p in paths)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if common(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
