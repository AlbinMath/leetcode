from typing import List
from bisect import bisect_left, bisect_right
from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        cnt = Counter(nums)
        ans = 0

        # Case 1: target is an existing value
        for v, c in cnt.items():
            inr = bisect_right(nums, v + k) - bisect_left(nums, v - k)
            ans = max(ans, c + min(numOperations, inr - c))

        # Case 2: target is any value; need a window of width 2k
        l = 0
        for r in range(n):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            ans = max(ans, min(numOperations, r - l + 1))

        return ans
