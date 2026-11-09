from typing import List

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        mx = 0
        count = 0
        for x in nums:
            if x >= mx:
                mx = x
                count += 1
        return count
