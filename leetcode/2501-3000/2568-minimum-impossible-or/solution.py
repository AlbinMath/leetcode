from typing import List

class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s = set(nums)
        p = 1
        while p in s:
            p <<= 1
        return p
