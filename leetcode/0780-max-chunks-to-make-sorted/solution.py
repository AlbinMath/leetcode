from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        mx = 0
        for i, x in enumerate(arr):
            mx = max(mx, x)
            if mx == i:
                chunks += 1
        return chunks
