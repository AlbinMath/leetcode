class Solution:
    def numSquares(self, n):
        dp = [0] + [float('inf')] * n
        for i in range(1, int(n**0.5) + 1):
            s = i * i
            for j in range(s, n + 1):
                dp[j] = min(dp[j], dp[j-s] + 1)
        return dp[n]
