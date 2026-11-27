class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (rollMax[j] + 1) for j in range(6)]
        for j in range(6):
            dp[j][1] = 1
            
        for _ in range(1, n):
            next_dp = [[0] * (rollMax[j] + 1) for j in range(6)]
            row_sums = [sum(dp[j]) % MOD for j in range(6)]
            total_prev = sum(row_sums) % MOD
            
            for j in range(6):
                next_dp[j][1] = (total_prev - row_sums[j]) % MOD
                
                for k in range(2, rollMax[j] + 1):
                    next_dp[j][k] = dp[j][k - 1]
                    
            dp = next_dp
            
        return sum(sum(row) for row in dp) % MOD
