from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        walls.sort()
        rs = sorted(zip(robots, distance))
        n = len(rs)
        INF = float('inf')

        def cnt(l, r):
            if l > r:
                return 0
            return bisect_right(walls, r) - bisect_left(walls, l)

        def left(i):
            p, d = rs[i]
            lo = p - d
            if i > 0:
                lo = max(lo, rs[i - 1][0] + 1)
            return lo, p

        def right(i):
            p, d = rs[i]
            hi = p + d
            if i < n - 1:
                hi = min(hi, rs[i + 1][0] - 1)
            return p, hi

        l0, r0 = left(0)
        a, b = right(0)
        dpL, dpR = cnt(l0, r0), cnt(a, b)

        for i in range(1, n):
            ll, lr = left(i)
            rl, rr = right(i)
            pl, pr = right(i - 1)
            overlap = cnt(max(pl, ll), min(pr, lr))
            newL = cnt(ll, lr) + max(dpL, dpR - overlap)
            newR = cnt(rl, rr) + max(dpL, dpR)
            dpL, dpR = newL, newR

        return max(dpL, dpR)
