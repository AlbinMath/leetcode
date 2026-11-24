from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        slopes = defaultdict(lambda: defaultdict(int))   # (dx,dy) -> {c: count}
        mids = defaultdict(int)                          # (sx,sy) -> count
        mids_slope = defaultdict(int)                    # (sx,sy,dx,dy) -> count

        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dx, dy = xj - xi, yj - yi
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                c = dx * yi - dy * xi
                slopes[(dx, dy)][c] += 1
                sx, sy = xi + xj, yi + yj
                mids[(sx, sy)] += 1
                mids_slope[(sx, sy, dx, dy)] += 1

        pairs = 0
        for lines in slopes.values():
            total = sum(lines.values())
            sq = sum(v * v for v in lines.values())
            pairs += (total * total - sq) // 2

        para = sum(m * (m - 1) // 2 for m in mids.values())
        para -= sum(m * (m - 1) // 2 for m in mids_slope.values())

        return pairs - para
