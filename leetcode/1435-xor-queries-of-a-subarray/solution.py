from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        p = [0] * (len(arr) + 1)
        for i, x in enumerate(arr):
            p[i + 1] = p[i] ^ x
        return [p[r + 1] ^ p[l] for l, r in queries]
