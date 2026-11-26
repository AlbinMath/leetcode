from collections import Counter
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr) // 2
        frequencies = sorted(Counter(arr).values(), reverse=True)
        
        removed = 0
        for set_size, freq in enumerate(frequencies, start=1):
            removed += freq
            if removed >= half:
                return set_size
                
        return 0
