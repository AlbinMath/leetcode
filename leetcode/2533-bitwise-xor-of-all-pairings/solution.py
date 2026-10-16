from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums2) % 2:
            for v in nums1:
                ans ^= v
        if len(nums1) % 2:
            for v in nums2:
                ans ^= v
        return ans
