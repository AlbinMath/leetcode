from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        ans = 0
        suffix_sum = 0
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if count > 0 and nums[i] * count > suffix_sum:
                ans += 1
            suffix_sum += nums[i]
            count += 1
        return ans
