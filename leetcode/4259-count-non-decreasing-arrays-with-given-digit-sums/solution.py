from typing import List

class Solution:
    def countArrays(self, digitSum: List[int]) -> int:
        MOD = 10**9 + 7
        M = 5001
        ds = [sum(map(int, str(v))) for v in range(M)]

        # first position: every value with matching digit sum counts once
        dp = [1 if ds[v] == digitSum[0] else 0 for v in range(M)]

        for i in range(1, len(digitSum)):
            target = digitSum[i]
            new = [0] * M
            run = 0
            for v in range(M):
                run = (run + dp[v]) % MOD      # sum of dp[u] for u <= v
                if ds[v] == target:
                    new[v] = run
            dp = new

        return sum(dp) % MOD
