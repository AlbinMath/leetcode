class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        pows = set()
        v = 1
        while v < (1 << n):
            pows.add(bin(v)[2:])
            v *= 5

        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] != INF and s[j:i] in pows:
                    dp[i] = min(dp[i], dp[j] + 1)
        return -1 if dp[n] == INF else dp[n]
