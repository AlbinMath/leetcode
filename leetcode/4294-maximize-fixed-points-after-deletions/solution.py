from bisect import bisect_left
from typing import List

class Solution:
    def maxFixedPoints(self, nums: List[int]) -> int:
        items = [(i - x, x) for i, x in enumerate(nums) if x <= i]
        items.sort()                       # b ascending, then a ascending
        tails = []
        for _, a in items:
            pos = bisect_left(tails, a)    # strictly increasing in a
            if pos == len(tails):
                tails.append(a)
            else:
                tails[pos] = a
        return len(tails)
