from typing import List

class Solution:
    def shadowPairs(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []  # [value, count, ns, idx]
        ans = 0
        for i in range(n - 1, -1, -1):
            x = nums[i]
            while stack and stack[-1][0] > x:
                stack.pop()
            if stack and stack[-1][0] == x:
                top = stack[-1]
                ns, eq = top[2], top[1]
                ans += ns - i - 1 - eq
                top[1] += 1
                top[3] = i
            else:
                ns = stack[-1][3] if stack else n
                ans += ns - i - 1
                stack.append([x, 1, ns, i])
        return ans
