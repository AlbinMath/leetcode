class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        n = len(nums)
        best = float('inf')
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur |= nums[j]
                if cur >= k:
                    if j - i + 1 < best:
                        best = j - i + 1
                    break
        return -1 if best == float('inf') else best
