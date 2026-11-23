from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        unique_nums = sorted(set(nums))
        
        max_keep = 0
        left = 0
        
        for right, val in enumerate(unique_nums):
            while val - unique_nums[left] >= n:
                left += 1
            if right - left + 1 > max_keep:
                max_keep = right - left + 1
                
        return n - max_keep
