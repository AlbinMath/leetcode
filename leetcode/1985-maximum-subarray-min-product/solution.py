from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, x in enumerate(nums):
            pre[i + 1] = pre[i] + x

        stack = []
        best = 0
        for j in range(n + 1):
            cur = nums[j] if j < n else 0
            while stack and nums[stack[-1]] >= cur:
                i = stack.pop()
                left = stack[-1] + 1 if stack else 0
                best = max(best, nums[i] * (pre[j] - pre[left]))
            stack.append(j)

        return best % (10**9 + 7)
