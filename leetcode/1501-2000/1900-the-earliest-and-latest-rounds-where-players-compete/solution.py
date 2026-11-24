from functools import lru_cache
from typing import List

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(maxsize=None)
        def go(n, a, b):
            if a + b == n + 1:
                return (1, 1)
            if a + b > n + 1:
                a, b = n + 1 - b, n + 1 - a
            m = (n + 1) // 2
            lo, hi = float('inf'), 0
            if 2 * b <= n + 1:
                for x in range(a):
                    na = x + 1
                    for y in range(b - a):
                        nb = na + y + 1
                        r = go(m, na, nb)
                        lo = min(lo, r[0] + 1)
                        hi = max(hi, r[1] + 1)
            else:
                c = n + 1 - b
                add = (b - c) // 2          # (k + 1) // 2 with k = b - c - 1
                for x in range(a):
                    na = x + 1
                    for y in range(c - a):
                        nb = na + y + add + 1
                        r = go(m, na, nb)
                        lo = min(lo, r[0] + 1)
                        hi = max(hi, r[1] + 1)
            return (lo, hi)

        a, b = sorted((firstPlayer, secondPlayer))
        return list(go(n, a, b))
