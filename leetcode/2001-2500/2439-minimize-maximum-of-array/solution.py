from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        total = 0
        for i, x in enumerate(nums, 1):
            total += x
            ans = max(ans, (total + i - 1) // i)
        return ans
