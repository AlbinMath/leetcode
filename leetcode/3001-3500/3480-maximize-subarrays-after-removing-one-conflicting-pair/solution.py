from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        by_r = [[] for _ in range(n + 1)]
        for i, (a, b) in enumerate(conflictingPairs):
            lo, hi = min(a, b), max(a, b)
            by_r[hi].append((lo, i))

        gain = [0] * len(conflictingPairs)
        best1 = best2 = 0
        idx = -1
        total = 0

        for r in range(1, n + 1):
            for lo, i in by_r[r]:
                if lo > best1:
                    best2 = best1
                    best1 = lo
                    idx = i
                elif lo > best2:
                    best2 = lo
            total += r - best1
            if idx != -1:
                gain[idx] += best1 - best2

        return total + max(gain)
