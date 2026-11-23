class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)
        for t in range(1, target + 1):
            n = t.bit_length()
            if (1 << n) - 1 == t:
                dp[t] = n
                continue
            # overshoot, then reverse
            dp[t] = n + 1 + dp[(1 << n) - 1 - t]
            # undershoot at n-1 accelerations, reverse, back up m, reverse again
            for m in range(n - 1):
                dist = t - ((1 << (n - 1)) - 1) + ((1 << m) - 1)
                dp[t] = min(dp[t], (n - 1) + 1 + m + 1 + dp[dist])
        return dp[target]
