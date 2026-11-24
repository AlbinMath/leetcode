class Solution:
    def maxNumOfMarkedIndices(self, nums):
        nums.sort()
        n = len(nums)

        def ok(k):
            return all(2 * nums[i] <= nums[n - k + i] for i in range(k))

        lo, hi = 0, n // 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return 2 * lo
