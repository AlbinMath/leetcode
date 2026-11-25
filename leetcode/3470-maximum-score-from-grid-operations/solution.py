class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        NEG = -10**18

        pre = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                pre[j][i + 1] = pre[j][i] + grid[i][j]

        # dp[a][b]: a = h[j-1], b = h[j]
        dp = [[NEG] * (n + 1) for _ in range(n + 1)]
        for b in range(n + 1):
            dp[0][b] = 0

        for j in range(n):
            p = pre[j]
            cs = range(n + 1) if j < n - 1 else [0]
            new = [[NEG] * (n + 1) for _ in range(n + 1)]

            for b in range(n + 1):
                pb = p[b]
                # prefix max of dp[a][b]
                pm = [NEG] * (n + 1)
                cur = NEG
                for a in range(n + 1):
                    cur = max(cur, dp[a][b])
                    pm[a] = cur
                # suffix max of dp[a][b] + S(b, a)
                sm = [NEG] * (n + 2)
                for a in range(n, -1, -1):
                    val = dp[a][b]
                    if val > NEG:
                        val += max(0, p[a] - pb)
                    sm[a] = max(sm[a + 1], val)

                for c in cs:
                    best = NEG
                    if pm[c] > NEG:
                        best = pm[c] + max(0, p[c] - pb)
                    best = max(best, sm[c + 1])
                    new[b][c] = best

            dp = new

        return max(dp[b][0] for b in range(n + 1))
