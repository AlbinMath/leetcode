from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        curr_sum = 0
        max_sum = 0
        
        for val in nums:
            while val in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            seen.add(val)
            curr_sum += val
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        return max_sum
