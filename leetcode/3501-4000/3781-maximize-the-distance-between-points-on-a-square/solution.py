from bisect import bisect_left
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        pos = []
        for x, y in points:
            if y == 0:
                pos.append(x)
            elif x == side:
                pos.append(side + y)
            elif y == side:
                pos.append(3 * side - x)
            else:
                pos.append(4 * side - y)
        pos.sort()
        n = len(pos)
        total = 4 * side

        def ok(d: int) -> bool:
            nxt = [bisect_left(pos, p + d) for p in pos]
            for i in range(n):
                j = i
                for _ in range(k - 1):
                    j = nxt[j]
                    if j >= n:
                        break
                else:
                    if pos[j] - pos[i] <= total - d:
                        return True
            return False

        lo, hi = 1, side
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
