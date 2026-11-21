class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        # cost[i][j]: changes to make s[i..j] a palindrome
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                inner = cost[i + 1][j - 1] if length > 2 else 0
                cost[i][j] = inner + (s[i] != s[j])

        INF = float('inf')
        # dp[p][i]: min changes for first i chars split into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(p, n + 1):
                for m in range(p - 1, i):
                    if dp[p - 1][m] + cost[m][i - 1] < dp[p][i]:
                        dp[p][i] = dp[p - 1][m] + cost[m][i - 1]

        return dp[k][n]
