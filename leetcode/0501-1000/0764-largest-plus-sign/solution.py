class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        dp = [[n] * n for _ in range(n)]
        for r, c in mines:
            dp[r][c] = 0
            
        for r in range(n):
            count = 0
            for c in range(n):
                count = 0 if dp[r][c] == 0 else count + 1
                dp[r][c] = min(dp[r][c], count)
                
            count = 0
            for c in range(n - 1, -1, -1):
                count = 0 if dp[r][c] == 0 else count + 1
                dp[r][c] = min(dp[r][c], count)
                
        ans = 0
        for c in range(n):
            count = 0
            for r in range(n):
                count = 0 if dp[r][c] == 0 else count + 1
                dp[r][c] = min(dp[r][c], count)
                
            count = 0
            for r in range(n - 1, -1, -1):
                count = 0 if dp[r][c] == 0 else count + 1
                dp[r][c] = min(dp[r][c], count)
                if dp[r][c] > ans:
                    ans = dp[r][c]
                    
        return ans
