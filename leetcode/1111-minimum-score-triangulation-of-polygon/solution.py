class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                base_prod = values[i] * values[j]
                dp[i][j] = min(
                    dp[i][k] + dp[k][j] + base_prod * values[k]
                    for k in range(i + 1, j)
                )
                
        return dp[0][n - 1]
