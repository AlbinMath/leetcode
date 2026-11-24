from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        p = [0] * (len(s) + 1)
        for i, ch in enumerate(s):
            p[i + 1] = p[i] ^ (1 << (ord(ch) - 97))

        return [(p[r + 1] ^ p[l]).bit_count() // 2 <= k for l, r, k in queries]
