from bisect import bisect_left, bisect_right

class Solution:
    def minLengthAfterRemovals(self, nums: list[int]) -> int:
        n = len(nums)
        mid_val = nums[n // 2]
        max_freq = bisect_right(nums, mid_val) - bisect_left(nums, mid_val)
        
        if max_freq > n // 2:
            return 2 * max_freq - n
            
        return n % 2
