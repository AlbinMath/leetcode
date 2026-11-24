from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, x in enumerate(nums):
            if not stack or x < nums[stack[-1]]:
                stack.append(i)

        ans = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                ans = max(ans, j - stack.pop())
            if not stack:
                break
        return ans
