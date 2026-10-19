from collections import Counter
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        rows = Counter(y for _, y in points)
        total = 0   # sum of segments over earlier rows
        ans = 0
        for c in rows.values():
            seg = c * (c - 1) // 2
            ans = (ans + seg * total) % MOD
            total = (total + seg) % MOD
        return ans
