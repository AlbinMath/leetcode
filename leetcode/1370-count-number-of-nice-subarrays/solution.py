from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = odd_count = valid_prefixes = total = 0
        
        for val in nums:
            if val & 1:
                odd_count += 1
                valid_prefixes = 0
                
            while odd_count == k:
                odd_count -= nums[left] & 1
                left += 1
                valid_prefixes += 1
                
            total += valid_prefixes
            
        return total
