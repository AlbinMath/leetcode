from bisect import bisect_left
from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0

        for h in houses:
            i = bisect_left(heaters, h)
            left = h - heaters[i - 1] if i > 0 else float('inf')
            right = heaters[i] - h if i < len(heaters) else float('inf')
            radius = max(radius, min(left, right))

        return radius
