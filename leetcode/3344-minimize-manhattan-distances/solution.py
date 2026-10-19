from typing import List

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        n = len(points)
        u = [x + y for x, y in points]
        v = [x - y for x, y in points]

        by_u = sorted(range(n), key=lambda i: u[i])
        by_v = sorted(range(n), key=lambda i: v[i])

        # candidates: the two smallest and two largest in each order
        # (two on each side so one survives after removing the other)
        cand = set(by_u[:2] + by_u[-2:] + by_v[:2] + by_v[-2:])

        def span(order, vals, skip):
            lo = order[0] if order[0] != skip else order[1]
            hi = order[-1] if order[-1] != skip else order[-2]
            return vals[hi] - vals[lo]

        best = float('inf')
        for c in cand:
            d = max(span(by_u, u, c), span(by_v, v, c))
            best = min(best, d)
        return best
