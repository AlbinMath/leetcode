from math import sqrt
from typing import List

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        best = 1
        eps = 1e-7
        for i in range(n):
            x1, y1 = darts[i]
            for j in range(i + 1, n):
                x2, y2 = darts[j]
                dx, dy = x2 - x1, y2 - y1
                d2 = dx * dx + dy * dy
                if d2 > 4 * r * r:
                    continue
                d = sqrt(d2)
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                h = sqrt(max(0.0, r * r - d2 / 4))
                ux, uy = -dy / d, dx / d
                for sign in (1, -1):
                    cx = mx + sign * h * ux
                    cy = my + sign * h * uy
                    cnt = 0
                    for x, y in darts:
                        if (x - cx) ** 2 + (y - cy) ** 2 <= r * r + eps:
                            cnt += 1
                    if cnt > best:
                        best = cnt
        return best
