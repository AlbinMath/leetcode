from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        groups = 1
        start = nums[0]
        for x in nums:
            if x - start > k:
                groups += 1
                start = x
        return groups
