from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = sum(nums)
        
        if k <= 1 or k == n:
            return 0
            
        curr_ones = sum(nums[:k])
        max_ones = curr_ones
        
        for i in range(1, n):
            right = i + k - 1
            if right >= n:
                right -= n
            curr_ones += nums[right] - nums[i - 1]
            if curr_ones > max_ones:
                max_ones = curr_ones
                
        return k - max_ones
