from collections import Counter

class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        freq = Counter(power)
        vals = sorted(freq.keys())
        m = len(vals)
        
        dp = [0] * m
        
        for i in range(m):
            curr_gain = vals[i] * freq[vals[i]]
            
            j = i - 1
            while j >= 0 and vals[i] - vals[j] <= 2:
                j -= 1
                
            if j >= 0:
                curr_gain += dp[j]
                
            dp[i] = max(dp[i - 1] if i > 0 else 0, curr_gain)
            
        return dp[-1]
