from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(S: int) -> int:
            if S < 0:
                return 0
            count = curr_sum = left = 0
            for right, val in enumerate(nums):
                curr_sum += val
                while curr_sum > S:
                    curr_sum -= nums[left]
                    left += 1
                count += right - left + 1
            return count
            
        return at_most(goal) - at_most(goal - 1)
