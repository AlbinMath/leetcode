from math import isqrt
from typing import List

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def closest(t: int) -> List[int]:
            for d in range(isqrt(t), 0, -1):
                if t % d == 0:
                    return [d, t // d]

        a = closest(num + 1)
        b = closest(num + 2)
        return a if abs(a[0] - a[1]) <= abs(b[0] - b[1]) else b
