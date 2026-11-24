from bisect import bisect_left, insort
from typing import List

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        seen = []
        ans = float('inf')

        for i in range(x, len(nums)):
            insort(seen, nums[i - x])
            v = nums[i]
            k = bisect_left(seen, v)
            if k < len(seen):
                ans = min(ans, seen[k] - v)
            if k > 0:
                ans = min(ans, v - seen[k - 1])
            if ans == 0:
                return 0

        return ans
