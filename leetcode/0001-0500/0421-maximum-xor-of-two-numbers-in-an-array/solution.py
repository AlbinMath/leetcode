from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for b in range(30, -1, -1):
            prefixes = {v >> b for v in nums}
            cand = (ans << 1) | 1
            if any((p ^ cand) in prefixes for p in prefixes):
                ans = cand
            else:
                ans <<= 1
        return ans
