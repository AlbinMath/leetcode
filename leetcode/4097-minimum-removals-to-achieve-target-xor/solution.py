class Solution(object):
    def minRemovals(self, nums, target):
        SIZE = 1 << 14
        if target >= SIZE:
            return -1
        NEG = -1
        dp = [NEG] * SIZE
        dp[0] = 0
        for v in nums:
            new = dp[:]
            for x in range(SIZE):
                if dp[x] != NEG:
                    y = x ^ v
                    if dp[x] + 1 > new[y]:
                        new[y] = dp[x] + 1
            dp = new
        if dp[target] == NEG:
            return -1
        return len(nums) - dp[target]
