from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_val = max(nums)
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num
        prev2 = 0  # dp[i - 2]
        prev1 = 0  # dp[i - 1]
        
        for pts in points:
            curr = max(prev1, prev2 + pts)
            prev2 = prev1
            prev1 = curr
            
        return prev1
