import heapq
import math
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Negate values to simulate a max-heap with Python's min-heap
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            if largest == 1:
                heapq.heappush(max_heap, -1)
                break
            heapq.heappush(max_heap, -math.isqrt(largest))
            
        return -sum(max_heap)
