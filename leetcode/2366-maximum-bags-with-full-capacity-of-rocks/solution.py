from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        need = sorted(c - r for c, r in zip(capacity, rocks))
        count = 0
        for x in need:
            if x > additionalRocks:
                break
            additionalRocks -= x
            count += 1
        return count
