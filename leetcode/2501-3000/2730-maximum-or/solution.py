class Solution(object):
    def maximumOr(self, nums, k):
        n = len(nums)
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] | nums[i]

        best = 0
        pre = 0
        for i in range(n):
            best = max(best, pre | (nums[i] << k) | suf[i + 1])
            pre |= nums[i]
        return best
