class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1):
            return -1

        P = [0] * (n + 1)
        for i, v in enumerate(stones):
            P[i + 1] = P[i] + v

        INF = float('inf')
        dp = [[[INF] * (k + 1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i][1] = 0

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for p in range(2, k + 1):
                    for m in range(i, j, k - 1):
                        c = dp[i][m][1] + dp[m + 1][j][p - 1]
                        if c < dp[i][j][p]:
                            dp[i][j][p] = c
                if dp[i][j][k] < INF:
                    dp[i][j][1] = dp[i][j][k] + P[j + 1] - P[i]

        return dp[0][n - 1][1]
