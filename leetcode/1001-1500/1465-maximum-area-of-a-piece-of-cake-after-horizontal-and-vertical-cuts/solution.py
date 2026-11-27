from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9 + 7

        def max_gap(cuts: List[int], limit: int) -> int:
            cuts = sorted(cuts)
            best = cuts[0]  # gap from 0 to the first cut
            for i in range(1, len(cuts)):
                best = max(best, cuts[i] - cuts[i - 1])
            return max(best, limit - cuts[-1])  # gap from the last cut to the edge

        return (max_gap(horizontalCuts, h) * max_gap(verticalCuts, w)) % MOD
