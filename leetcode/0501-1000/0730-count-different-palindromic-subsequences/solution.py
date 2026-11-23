class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        # nxt[i][c]: first index >= i with letter c (n if none)
        # prv[i][c]: last index <= i with letter c (-1 if none)
        nxt = [[n] * 4 for _ in range(n + 2)]
        prv = [[-1] * 4 for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            nxt[i] = nxt[i + 1][:]
            nxt[i][ord(s[i]) - 97] = i
        for i in range(n):
            prv[i] = prv[i - 1][:] if i > 0 else [-1] * 4
            prv[i][ord(s[i]) - 97] = i

        # dp[i][j] with empty ranges (i > j) equal to 0
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        def get(i, j):
            return dp[i][j] if i <= j else 0

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] != s[j]:
                    dp[i][j] = (get(i + 1, j) + get(i, j - 1) - get(i + 1, j - 1)) % MOD
                else:
                    c = ord(s[i]) - 97
                    lo = nxt[i + 1][c]
                    hi = prv[j - 1][c]
                    inner = get(i + 1, j - 1)
                    if lo > j - 1 or lo > hi:        # no c strictly inside
                        dp[i][j] = (2 * inner + 2) % MOD
                    elif lo == hi:                   # exactly one c inside
                        dp[i][j] = (2 * inner + 1) % MOD
                    else:                            # two or more c inside
                        dp[i][j] = (2 * inner - get(lo + 1, hi - 1)) % MOD

        return dp[0][n - 1] % MOD
