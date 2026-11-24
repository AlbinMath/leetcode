from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        ans = 0
        prev = 0
        for a, b in zip(nums, target):
            cur = b - a
            if cur > 0:
                ans += max(0, cur - max(prev, 0))
            elif cur < 0:
                ans += max(0, -cur - max(-prev, 0))
            prev = cur
        return ans
