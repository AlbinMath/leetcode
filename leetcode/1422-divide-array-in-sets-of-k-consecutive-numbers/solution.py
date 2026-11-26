from collections import Counter
from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
            
        counts = Counter(nums)
        
        for start in sorted(counts):
            needed = counts[start]
            if needed > 0:
                for num in range(start, start + k):
                    if counts[num] < needed:
                        return False
                    counts[num] -= needed
                    
        return True
