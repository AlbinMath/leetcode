from typing import List
from collections import defaultdict

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        positions = defaultdict(list)
        for i, x in enumerate(nums):
            positions[x].append(i)

        ans = 0
        for pos in positions.values():
            l = 0
            for r in range(len(pos)):
                while (pos[r] - pos[l] + 1) - (r - l + 1) > k:
                    l += 1
                ans = max(ans, r - l + 1)
        return ans
