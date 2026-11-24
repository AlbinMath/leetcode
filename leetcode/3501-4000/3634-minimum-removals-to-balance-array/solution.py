from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        best = 0
        for r, x in enumerate(nums):
            while x > k * nums[l]:
                l += 1
            best = max(best, r - l + 1)
        return len(nums) - best
