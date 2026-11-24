from typing import List

class Solution:
    def maxValidPairSum(self, nums: List[int], k: int) -> int:
        ans = 0
        best = 0
        for j in range(k, len(nums)):
            best = max(best, nums[j - k])
            ans = max(ans, best + nums[j])
        return ans
