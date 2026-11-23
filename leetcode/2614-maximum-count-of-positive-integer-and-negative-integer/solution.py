from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        neg = bisect_left(nums, 0)
        pos = len(nums) - bisect_right(nums, 0)
        
        return max(neg, pos)
