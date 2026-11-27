from typing import List

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        base = 0
        min_hi = float('inf')
        max_lo = float('-inf')
        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            base += abs(a - b)
            min_hi = min(min_hi, max(a, b))
            max_lo = max(max_lo, min(a, b))

        gain = max(0, 2 * (max_lo - min_hi))
        for r in range(n - 1):
            gain = max(gain, abs(nums[0] - nums[r + 1]) - abs(nums[r] - nums[r + 1]))
        for l in range(1, n):
            gain = max(gain, abs(nums[n - 1] - nums[l - 1]) - abs(nums[l] - nums[l - 1]))

        return base + gain
