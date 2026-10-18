from bisect import bisect_left
from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def occurrences(p: str) -> List[int]:
            m = len(p)
            return [i for i in range(len(s) - m + 1) if s[i:i + m] == p]

        A = occurrences(a)
        B = occurrences(b)

        res = []
        for i in A:
            # smallest j in B with j >= i - k
            pos = bisect_left(B, i - k)
            if pos < len(B) and B[pos] <= i + k:
                res.append(i)
        return res
