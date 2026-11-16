class Solution(object):
    def minCost(self, nums, x):
        n = len(nums)
        min_cost = list(nums)
        ans = sum(min_cost)

        for k in range(1, n):
            for i in range(n):
                prev_idx = (i - k) % n
                if nums[prev_idx] < min_cost[i]:
                    min_cost[i] = nums[prev_idx]
            ans = min(ans, k * x + sum(min_cost))

        return ans
