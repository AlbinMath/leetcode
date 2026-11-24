from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        prev = 0      # length of the previous run
        cur = 1       # length of the current run

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += 1
            else:
                ans = max(ans, cur // 2, min(prev, cur))
                prev, cur = cur, 1

        ans = max(ans, cur // 2, min(prev, cur))
        return ans
