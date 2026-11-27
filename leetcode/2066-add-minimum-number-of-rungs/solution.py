from typing import List

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        prev = 0
        added = 0
        for r in rungs:
            added += (r - prev - 1) // dist
            prev = r
        return added
