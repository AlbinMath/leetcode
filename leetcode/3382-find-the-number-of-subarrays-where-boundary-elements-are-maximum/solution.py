from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        stack = []  # [value, count], values non-increasing
        ans = 0
        for x in nums:
            while stack and stack[-1][0] < x:
                stack.pop()
            if stack and stack[-1][0] == x:
                stack[-1][1] += 1
            else:
                stack.append([x, 1])
            ans += stack[-1][1]
        return ans
