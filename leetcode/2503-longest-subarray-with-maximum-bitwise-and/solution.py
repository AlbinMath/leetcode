from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        best = cur = 0
        for v in nums:
            if v == m:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return best
