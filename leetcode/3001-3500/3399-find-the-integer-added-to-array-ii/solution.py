from typing import List

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        ans = float('inf')

        for i in range(3):
            x = nums2[0] - nums1[i]
            j = 0
            for v in nums1:
                if j < len(nums2) and v + x == nums2[j]:
                    j += 1
            if j == len(nums2):
                ans = min(ans, x)

        return ans
