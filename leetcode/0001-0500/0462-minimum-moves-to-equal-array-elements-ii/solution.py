from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        med = nums[len(nums) // 2]
        return sum(abs(v - med) for v in nums)
