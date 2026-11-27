from typing import List

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return nums[0]
        if n == 1:
            return -1 if k % 2 == 1 else nums[0]
        best = -1
        if k >= 2:
            best = max(nums[:min(k - 1, n)])
        if k < n:
            best = max(best, nums[k])
        return best
