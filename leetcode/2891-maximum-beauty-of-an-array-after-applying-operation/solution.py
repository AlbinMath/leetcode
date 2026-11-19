from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        ans = 0
        for r, x in enumerate(nums):
            while x - nums[l] > 2 * k:
                l += 1
            ans = max(ans, r - l + 1)
        return ans
