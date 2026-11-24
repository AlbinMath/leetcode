from bisect import bisect_right
from typing import List

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10**9 + 7
        packages.sort()
        n = len(packages)
        total_pkg = sum(packages)
        max_pkg = packages[-1]

        best = float('inf')
        for supplier in boxes:
            supplier.sort()
            if supplier[-1] < max_pkg:
                continue

            used = 0
            prev = 0
            for b in supplier:
                idx = bisect_right(packages, b)
                if idx > prev:
                    used += b * (idx - prev)
                    prev = idx
                if prev == n:
                    break

            best = min(best, used - total_pkg)

        return -1 if best == float('inf') else best % MOD
