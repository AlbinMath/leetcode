class Solution:
    def minCost(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            freq = [0] * n
            trimmed_len = 0
            
            for j in range(i - 1, -1, -1):
                val = nums[j]
                freq[val] += 1
                
                if freq[val] == 2:
                    trimmed_len += 2
                elif freq[val] > 2:
                    trimmed_len += 1
                    
                cost = dp[j] + k + trimmed_len
                if cost < dp[i]:
                    dp[i] = cost
                    
        return dp[n]
