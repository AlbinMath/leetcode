class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            ndp = [0] * (k + 1)
            s = 0
            for j in range(k + 1):
                s = (s + dp[j]) % MOD
                if j >= i:
                    s = (s - dp[j - i]) % MOD
                ndp[j] = s
            dp = ndp
        return dp[k]
