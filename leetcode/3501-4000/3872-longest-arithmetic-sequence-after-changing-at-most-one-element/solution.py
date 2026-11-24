from typing import List

class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        L = [1] * n
        R = [1] * n
        L[1] = 2
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                L[i] = L[i - 1] + 1
            else:
                L[i] = 2
        R[n - 2] = 2
        for i in range(n - 3, -1, -1):
            if nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1]:
                R[i] = R[i + 1] + 1
            else:
                R[i] = 2

        ans = max(L)
        for k in range(n):
            if k >= 1:
                ans = max(ans, L[k - 1] + 1)
            if k + 1 < n:
                ans = max(ans, R[k + 1] + 1)
            if 1 <= k <= n - 2:
                diff = nums[k + 1] - nums[k - 1]
                if diff % 2 == 0:
                    d = diff // 2
                    left = L[k - 1] if k >= 2 and nums[k - 1] - nums[k - 2] == d else 1
                    right = R[k + 1] if k + 2 < n and nums[k + 2] - nums[k + 1] == d else 1
                    ans = max(ans, left + 1 + right)
        return ans
