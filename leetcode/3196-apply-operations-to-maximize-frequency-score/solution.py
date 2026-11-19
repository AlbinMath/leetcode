from typing import List

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        P = [0] * (n + 1)
        for i, x in enumerate(nums):
            P[i + 1] = P[i] + x

        def cost(l: int, r: int) -> int:
            mid = (l + r) // 2
            m = nums[mid]
            left = m * (mid - l) - (P[mid] - P[l])
            right = (P[r + 1] - P[mid + 1]) - m * (r - mid)
            return left + right

        ans = 0
        l = 0
        for r in range(n):
            while cost(l, r) > k:
                l += 1
            ans = max(ans, r - l + 1)
        return ans
