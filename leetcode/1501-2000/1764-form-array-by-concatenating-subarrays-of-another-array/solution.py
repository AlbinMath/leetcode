from typing import List

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        pos = 0
        n = len(nums)
        for g in groups:
            m = len(g)
            found = False
            while pos + m <= n:
                if nums[pos:pos + m] == g:
                    pos += m
                    found = True
                    break
                pos += 1
            if not found:
                return False
        return True
