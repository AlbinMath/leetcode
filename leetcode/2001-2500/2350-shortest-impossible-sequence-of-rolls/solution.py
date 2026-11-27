from typing import List

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        segments = 0
        for x in rolls:
            seen.add(x)
            if len(seen) == k:
                segments += 1
                seen.clear()
        return segments + 1
