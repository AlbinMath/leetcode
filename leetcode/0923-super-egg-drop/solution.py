class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [0] * (k + 1)   # dp[j] = floors coverable with j eggs and current m moves
        m = 0

        while dp[k] < n:
            m += 1
            # update right to left so dp[j-1] is still the previous move's value
            for j in range(k, 0, -1):
                dp[j] = dp[j] + dp[j - 1] + 1

        return m
