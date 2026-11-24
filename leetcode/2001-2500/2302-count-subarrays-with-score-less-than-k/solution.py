from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        window_sum = 0
        total = 0
        
        for right, val in enumerate(nums):
            window_sum += val
            while left <= right and window_sum * (right - left + 1) >= k:
                window_sum -= nums[left]
                left += 1
            total += right - left + 1
            
        return total
