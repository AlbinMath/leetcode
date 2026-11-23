from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        for i, x in enumerate(nums):
            while stack and stack[-1] > x and len(stack) + n - i > k:
                stack.pop()
            if len(stack) < k:
                stack.append(x)
        return stack
