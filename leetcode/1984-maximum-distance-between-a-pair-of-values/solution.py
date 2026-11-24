from bisect import bisect_left

class Solution:
    def maxDistance(self, nums1, nums2):
        neg2 = [-x for x in nums2]          # non-decreasing
        best = 0
        for i, x in enumerate(nums1):
            # count of j with nums2[j] >= x  <=>  -nums2[j] <= -x
            j = bisect_left(neg2, -x + 1) - 1
            if j >= i:
                best = max(best, j - i)
        return best
