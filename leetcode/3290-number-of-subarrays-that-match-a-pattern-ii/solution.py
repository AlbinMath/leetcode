from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        d = [(nums[i + 1] > nums[i]) - (nums[i + 1] < nums[i])
             for i in range(len(nums) - 1)]
        m = len(pattern)

        # KMP failure function for pattern
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j and pattern[i] != pattern[j]:
                j = fail[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            fail[i] = j

        # scan d, counting full matches
        count = 0
        j = 0
        for x in d:
            while j and x != pattern[j]:
                j = fail[j - 1]
            if x == pattern[j]:
                j += 1
            if j == m:
                count += 1
                j = fail[j - 1]
        return count
