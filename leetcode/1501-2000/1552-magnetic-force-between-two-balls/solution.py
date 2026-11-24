from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def can_place(d: int) -> bool:
            count, last = 1, position[0]
            for i in range(1, n):
                if position[i] - last >= d:
                    count += 1
                    last = position[i]
                    if count == m:
                        return True
            return False

        lo, hi = 1, (position[-1] - position[0]) // (m - 1)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_place(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
