from collections import defaultdict
from typing import List

class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        P = [0] * (n + 1)
        for i, v in enumerate(capacity):
            P[i + 1] = P[i] + v

        cnt = defaultdict(int)
        res = 0
        for r in range(2, n):
            l = r - 2
            cnt[(capacity[l], P[l + 1])] += 1
            v = capacity[r]
            res += cnt.get((v, P[r] - v), 0)
        return res
