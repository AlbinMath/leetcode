from math import atan2, degrees
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        px, py = location
        same = 0
        angles = []
        for x, y in points:
            if x == px and y == py:
                same += 1
            else:
                angles.append(degrees(atan2(y - py, x - px)))
        angles.sort()
        angles += [a + 360 for a in angles]

        eps = 1e-9
        best = 0
        left = 0
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle + eps:
                left += 1
            best = max(best, right - left + 1)
        return best + same
