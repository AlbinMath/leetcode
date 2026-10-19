from math import hypot
from typing import List

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        n = len(positions)
        x = sum(p[0] for p in positions) / n
        y = sum(p[1] for p in positions) / n

        def total(cx: float, cy: float) -> float:
            return sum(hypot(cx - px, cy - py) for px, py in positions)

        best = total(x, y)
        step = 100.0
        while step > 1e-7:
            moved = False
            for dx, dy in ((step, 0), (-step, 0), (0, step), (0, -step)):
                nx, ny = x + dx, y + dy
                cur = total(nx, ny)
                if cur < best:
                    best, x, y = cur, nx, ny
                    moved = True
                    break
            if not moved:
                step /= 2
        return best
