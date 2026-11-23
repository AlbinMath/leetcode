from typing import List

class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        end_hi = [1] * n
        end_lo = [1] * n
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                end_hi[i] = end_lo[i - 1] + 1
            elif nums[i - 1] > nums[i]:
                end_lo[i] = end_hi[i - 1] + 1

        start_hi = [1] * n
        start_lo = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                start_hi[i] = start_lo[i + 1] + 1
            elif nums[i] < nums[i + 1]:
                start_lo[i] = start_hi[i + 1] + 1

        ans = max(max(end_hi), max(end_lo))
        for k in range(1, n - 1):
            a, b = nums[k - 1], nums[k + 1]
            if a < b:
                ans = max(ans, end_lo[k - 1] + start_hi[k + 1])
            elif a > b:
                ans = max(ans, end_hi[k - 1] + start_lo[k + 1])
        return ans
