
class Solution:
    def stoneGameVII(self, stones):
        n = len(stones)
        pre = [0] * (n + 1)
        for i, x in enumerate(stones):
            pre[i + 1] = pre[i] + x

        dp = [0] * n
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                left = pre[j + 1] - pre[i + 1] - dp[i + 1]
                right = pre[j] - pre[i] - dp[i]
                dp[i] = max(left, right)

        return dp[0]

