from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c1, c2 = Counter(basket1), Counter(basket2)
        total = c1 + c2
        for v, c in total.items():
            if c % 2:
                return -1
        m = min(total)
        extra = []
        for v in total:
            d = c1[v] - c2[v]
            extra.extend([v] * (abs(d) // 2))
        extra.sort()
        k = len(extra) // 2
        return sum(min(x, 2 * m) for x in extra[:k])
