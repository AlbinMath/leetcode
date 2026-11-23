class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        dp = [0] * n

        for j in range(n):
            dp[j] = j  # worst case: cut between every character
            for i in range(j + 1):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
                    if i == 0:
                        dp[j] = 0
                    else:
                        dp[j] = min(dp[j], dp[i - 1] + 1)

        return dp[n - 1]
