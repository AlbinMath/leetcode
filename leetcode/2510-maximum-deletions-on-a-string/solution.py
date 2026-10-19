class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        # lcp[i][j] = longest common prefix of s[i:] and s[j:]
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if s[i] == s[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        dp = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            best = 1
            for ln in range(1, (n - i) // 2 + 1):
                if lcp[i][i + ln] >= ln:
                    best = max(best, 1 + dp[i + ln])
            dp[i] = best
        return dp[0]
