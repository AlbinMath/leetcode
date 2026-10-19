from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        count = 0
        for i in range(n - m):
            ok = True
            for k in range(m):
                a, b = nums[i + k], nums[i + k + 1]
                diff = (b > a) - (b < a)      # 1, 0, or -1
                if diff != pattern[k]:
                    ok = False
                    break
            if ok:
                count += 1
        return count
