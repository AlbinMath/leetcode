class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        ans = 0
        for _ in range(maxMove):
            nxt = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    v = dp[r][c]
                    if v == 0:
                        continue
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            nxt[nr][nc] = (nxt[nr][nc] + v) % MOD
                        else:
                            ans = (ans + v) % MOD
            dp = nxt
        return ans
