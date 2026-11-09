from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []  # (value, steps until removed)
        ans = 0
        for x in nums:
            cur = 0
            while stack and stack[-1][0] <= x:
                cur = max(cur, stack.pop()[1])
            cur = cur + 1 if stack else 0
            ans = max(ans, cur)
            stack.append((x, cur))
        return ans
