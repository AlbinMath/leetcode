from typing import List

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        R, C = len(pizza), len(pizza[0])

        apples = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                apples[r][c] = (
                    (pizza[r][c] == 'A')
                    + apples[r + 1][c]
                    + apples[r][c + 1]
                    - apples[r + 1][c + 1]
                )

        dp = [[1 if apples[r][c] > 0 else 0 for c in range(C)] for r in range(R)]

        for _ in range(2, k + 1):
            new = [[0] * C for _ in range(R)]
            for r in range(R):
                for c in range(C):
                    total = 0
                    for i in range(r + 1, R):
                        if apples[r][c] - apples[i][c] > 0:
                            total += dp[i][c]
                    for i in range(c + 1, C):
                        if apples[r][c] - apples[r][i] > 0:
                            total += dp[r][i]
                    new[r][c] = total % MOD
            dp = new

        return dp[0][0]
