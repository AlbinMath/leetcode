class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        max_pos = min(arrLen - 1, steps // 2)
        
        dp = [0] * (max_pos + 1)
        dp[0] = 1
        
        for _ in range(steps):
            next_dp = [0] * (max_pos + 1)
            for i in range(max_pos + 1):
                ways = dp[i]
                if i > 0:
                    ways += dp[i - 1]
                if i < max_pos:
                    ways += dp[i + 1]
                next_dp[i] = ways % MOD
            dp = next_dp
            
        return dp[0]
