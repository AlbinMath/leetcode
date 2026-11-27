class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        
        dp = [0] * (m + 1)
        
        for op in range(m - 1, -1, -1):
            mult = multipliers[op]
            for left in range(op + 1):
                right_idx = n - 1 - (op - left)
                pick_left = mult * nums[left] + dp[left + 1]
                pick_right = mult * nums[right_idx] + dp[left]
                dp[left] = pick_left if pick_left > pick_right else pick_right
                
        return dp[0]
