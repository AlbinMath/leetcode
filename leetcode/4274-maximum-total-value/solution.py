from typing import List

class Solution:
    def maxTotalValue(self, value: List[int], decay: List[int], m: int) -> int:
        MOD = 10**9 + 7

        def cnt(T):
            total = 0
            for v, d in zip(value, decay):
                if v >= T:
                    total += (v - T) // d + 1
            return total

        def series(T):
            # sum and count of all gains >= T
            s = c = 0
            for v, d in zip(value, decay):
                if v >= T:
                    k = (v - T) // d + 1
                    s += k * v - d * k * (k - 1) // 2
                    c += k
            return s, c

        if cnt(1) <= m:
            return series(1)[0] % MOD

        # largest T with cnt(T) >= m (cnt(1) > m, so T=1 qualifies)
        lo, hi = 1, max(value)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if cnt(mid) >= m:
                lo = mid
            else:
                hi = mid - 1
        T = lo

        s, c = series(T + 1)        # all gains strictly greater than T
        return (s + (m - c) * T) % MOD
