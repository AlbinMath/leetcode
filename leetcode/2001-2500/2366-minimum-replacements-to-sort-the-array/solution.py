from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        limit = nums[-1]
        ops = 0
        for i in range(len(nums) - 2, -1, -1):
            x = nums[i]
            if x <= limit:
                limit = x
            else:
                parts = (x + limit - 1) // limit
                ops += parts - 1
                limit = x // parts
        return ops
