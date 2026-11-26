from typing import List

class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(nums[i], suf[i + 1])

        pre = 0
        best = float('-inf')
        for i in range(n - 1):
            pre += nums[i]
            best = max(best, pre - suf[i + 1])
        return best
