from math import acos, degrees
from typing import List

class Solution:
    def internalAngles(self, sides: List[int]) -> List[float]:
        a, b, c = sorted(sides)
        if a + b <= c:
            return []

        def angle(opp, s1, s2):
            cos_v = (s1 * s1 + s2 * s2 - opp * opp) / (2 * s1 * s2)
            cos_v = max(-1.0, min(1.0, cos_v))   # guard against float drift
            return degrees(acos(cos_v))

        return sorted([angle(a, b, c), angle(b, a, c), angle(c, a, b)])
