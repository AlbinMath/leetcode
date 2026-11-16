from typing import List

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        full = (1 << n) - 1

        ok = [[nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0
               for j in range(n)] for i in range(n)]

        dp = [[0] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 1

        for mask in range(1, 1 << n):
            for last in range(n):
                cur = dp[mask][last]
                if cur == 0:
                    continue
                for j in range(n):
                    if mask >> j & 1 or not ok[last][j]:
                        continue
                    nm = mask | (1 << j)
                    dp[nm][j] = (dp[nm][j] + cur) % MOD

        return sum(dp[full]) % MOD
