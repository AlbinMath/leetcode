class Solution(object):
    def minNumber(self, nums1, nums2):
        common = set(nums1) & set(nums2)
        if common:
            return min(common)
            
        a, b = min(nums1), min(nums2)
        return min(a, b) * 10 + max(a, b)
