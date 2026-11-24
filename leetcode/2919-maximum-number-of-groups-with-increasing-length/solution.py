from typing import List

class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        total = 0
        groups = 0
        for x in usageLimits:
            total += x
            if total >= (groups + 1) * (groups + 2) // 2:
                groups += 1
        return groups
