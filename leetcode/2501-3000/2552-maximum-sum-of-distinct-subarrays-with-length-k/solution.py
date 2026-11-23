from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        curr_sum = 0
        max_sum = 0
        
        for i, val in enumerate(nums):
            curr_sum += val
            freq[val] += 1
            
            if i >= k:
                out_val = nums[i - k]
                curr_sum -= out_val
                freq[out_val] -= 1
                if freq[out_val] == 0:
                    del freq[out_val]
                    
            if i >= k - 1 and len(freq) == k and curr_sum > max_sum:
                max_sum = curr_sum
                
        return max_sum
