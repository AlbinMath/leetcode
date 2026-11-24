from bisect import bisect_left
from typing import List

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        sorted1 = sorted(nums1)
        n = len(nums1)

        total = 0
        best_gain = 0

        for a, b in zip(nums1, nums2):
            old = abs(a - b)
            total += old

            k = bisect_left(sorted1, b)
            new = old
            if k < n:
                new = min(new, sorted1[k] - b)
            if k > 0:
                new = min(new, b - sorted1[k - 1])

            best_gain = max(best_gain, old - new)

        return (total - best_gain) % MOD
