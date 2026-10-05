class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [0] * n

        for row in range(m):
            for col in range(n):

                if row == 0 and col == 0:
                    dp[col] = grid[row][col]

                elif row == 0:
                    dp[col] = dp[col - 1] + grid[row][col]

                elif col == 0:
                    dp[col] = dp[col] + grid[row][col]

                else:
                    dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]

        return dp[n - 1]
