from typing import List

class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for r, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                l = stack.pop()
                if r - l >= 2:
                    ans += 1
            if stack and r - stack[-1] >= 2:
                ans += 1
            stack.append(r)
        return ans
