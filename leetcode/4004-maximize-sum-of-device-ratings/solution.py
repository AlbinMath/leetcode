import heapq
from typing import List

class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        m, n = len(units), len(units[0])
        mins = [min(r) for r in units]
        S = sum(mins)
        if n == 1 or m == 1:
            return S

        d = []
        for r in units:
            a, b = heapq.nsmallest(2, r)
            d.append(b - a)

        g = min(range(m), key=lambda i: mins[i])
        total_d = sum(d)

        # Option A: g is the receiver
        res = S + total_d - d[g]

        # Option B: g gives too, some other s receives
        for s in range(m):
            if s != g:
                res = max(res, S + total_d - d[s] - (mins[s] - mins[g]))

        return res
