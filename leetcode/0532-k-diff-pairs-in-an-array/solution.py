from collections import Counter
from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)

        if k == 0:
            return sum(1 for c in freq.values() if c > 1)

        return sum(1 for x in freq if x + k in freq)
