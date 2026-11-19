from typing import List

class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for k in range(n + 1):
            if k > 0 and nums[k - 1] >= k:
                continue
            if k < n and nums[k] <= k:
                continue
            ans += 1
        return ans
