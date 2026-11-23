class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1
        for _ in range(n):
            nd = [[0] * 3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    v = dp[a][l]
                    if not v:
                        continue
                    nd[a][0] = (nd[a][0] + v) % MOD          # P
                    if l < 2:
                        nd[a][l + 1] = (nd[a][l + 1] + v) % MOD  # L
                    if a == 0:
                        nd[1][0] = (nd[1][0] + v) % MOD      # A
            dp = nd
        return sum(sum(row) for row in dp) % MOD
