class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n or target > n * k:
            return 0
            
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for dice in range(1, n + 1):
            next_dp = [0] * (target + 1)
            # Sum with `dice` dice is bounded between `dice` and `min(dice * k, target)`
            for s in range(dice, min(dice * k, target) + 1):
                for face in range(1, min(k, s) + 1):
                    next_dp[s] = (next_dp[s] + dp[s - face]) % MOD
            dp = next_dp
            
        return dp[target]
