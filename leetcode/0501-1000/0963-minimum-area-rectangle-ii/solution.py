from collections import defaultdict
from math import hypot
from typing import List

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        groups = defaultdict(list)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                key = (x1 + x2, y1 + y2, (x1 - x2) ** 2 + (y1 - y2) ** 2)
                groups[key].append((i, j))

        best = float('inf')
        for pairs in groups.values():
            m = len(pairs)
            for a in range(m):
                i, _ = pairs[a]
                x1, y1 = points[i]
                for b in range(a + 1, m):
                    k, l = pairs[b]
                    x3, y3 = points[k]
                    x4, y4 = points[l]
                    area = (hypot(x3 - x1, y3 - y1) *
                            hypot(x4 - x1, y4 - y1))
                    best = min(best, area)
        return 0 if best == float('inf') else best
