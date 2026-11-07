from math import gcd

class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 6

        dp = [[0] * 7 for _ in range(7)]
        for a in range(1, 7):
            for b in range(1, 7):
                if a != b and gcd(a, b) == 1:
                    dp[a][b] = 1

        for _ in range(n - 2):
            new = [[0] * 7 for _ in range(7)]
            for a in range(1, 7):
                for b in range(1, 7):
                    ways = dp[a][b]
                    if not ways:
                        continue
                    for c in range(1, 7):
                        if c != a and c != b and gcd(b, c) == 1:
                            new[b][c] = (new[b][c] + ways) % MOD
            dp = new

        return sum(sum(row) for row in dp) % MOD
