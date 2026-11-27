from typing import List

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        i = j = 0
        n, m = len(nums1), len(nums2)
        s1 = s2 = 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                s1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                s2 += nums2[j]
                j += 1
            else:
                best = max(s1, s2) + nums1[i]
                s1 = s2 = best
                i += 1
                j += 1
        while i < n:
            s1 += nums1[i]
            i += 1
        while j < m:
            s2 += nums2[j]
            j += 1
        return max(s1, s2) % MOD
