class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        N = [0] * (n + 1)
        C = [0] * (n + 1)
        for i in range(n):
            N[i + 1] = N[i] + nums[i]
            C[i + 1] = C[i] + cost[i]
        T = C[n]

        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            best = INF
            for j in range(i):
                v = dp[j] + N[i] * (C[i] - C[j]) + k * (T - C[j])
                if v < best:
                    best = v
            dp[i] = best
        return dp[n]
