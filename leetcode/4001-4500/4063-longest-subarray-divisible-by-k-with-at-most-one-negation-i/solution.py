from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        best = 0
        for l in range(n):
            S = 0
            seen = set()
            for r in range(l, n):
                x = nums[r]
                S += x
                seen.add((2 * x) % k)
                rem = S % k
                if rem == 0 or rem in seen:
                    best = max(best, r - l + 1)
        return best
