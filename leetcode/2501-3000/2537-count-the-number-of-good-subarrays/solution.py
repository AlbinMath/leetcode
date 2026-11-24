from typing import List
from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        left = 0
        pairs = 0
        total = 0
        
        for right, val in enumerate(nums):
            pairs += freq[val]
            freq[val] += 1
            
            while pairs >= k:
                total += n - right
                left_val = nums[left]
                freq[left_val] -= 1
                pairs -= freq[left_val]
                left += 1
                
        return total
