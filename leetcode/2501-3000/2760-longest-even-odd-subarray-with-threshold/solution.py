from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        curr_len = 0
        max_len = 0
        
        for i, val in enumerate(nums):
            if val > threshold:
                curr_len = 0
            elif curr_len > 0 and (val & 1) != (nums[i - 1] & 1):
                curr_len += 1
            else:
                curr_len = 1 if (val & 1) == 0 else 0
                
            if curr_len > max_len:
                max_len = curr_len
                
        return max_len
