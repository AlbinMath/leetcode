from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        best = 1
        for i in range(n):
            x1, y1 = points[i]
            cnt = defaultdict(int)
            for j in range(i + 1, n):
                dx = points[j][0] - x1
                dy = points[j][1] - y1
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                cnt[(dx, dy)] += 1
            if cnt:
                best = max(best, max(cnt.values()) + 1)
        return best
