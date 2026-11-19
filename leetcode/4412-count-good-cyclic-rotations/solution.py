from typing import List

class Solution:
    def countGoodRotations(self, nums: List[int]) -> int:
        n = len(nums)
        h = n // 2
        total = sum(nums)
        w = sum(nums[:h])
        ans = 0
        for r in range(n):
            if 2 * w > total:
                ans += 1
            w += nums[(r + h) % n] - nums[r]
        return ans
