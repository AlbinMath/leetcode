class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        P = [0] * (n + 1)
        for i, v in enumerate(nums):
            P[i + 1] = P[i] + v

        dp = [P[i] / i if i else 0 for i in range(n + 1)]  # one group

        for g in range(2, k + 1):
            new = [0.0] * (n + 1)
            for i in range(g, n + 1):
                best = 0.0
                for j in range(g - 1, i):
                    best = max(best, dp[j] + (P[i] - P[j]) / (i - j))
                new[i] = best
            dp = new

        return dp[n]
