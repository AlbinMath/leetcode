from collections import Counter
from typing import List

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        for x in sorted(counts, key=abs):
            if counts[x] > counts[2 * x]:
                return False
            counts[2 * x] -= counts[x]
            
        return True
