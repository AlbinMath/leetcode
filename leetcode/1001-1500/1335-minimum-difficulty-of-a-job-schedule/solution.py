class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
            
        dp = [float('inf')] * (n + 1)
        curr_max = 0
        for i in range(1, n + 1):
            curr_max = max(curr_max, jobDifficulty[i - 1])
            dp[i] = curr_max
            
        for day in range(2, d + 1):
            next_dp = [float('inf')] * (n + 1)
            for i in range(day, n + 1):
                max_diff = 0
                for j in range(i - 1, day - 2, -1):
                    max_diff = max(max_diff, jobDifficulty[j])
                    next_dp[i] = min(next_dp[i], dp[j] + max_diff)
            dp = next_dp
            
        return dp[n]
