from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def occurrences(p: str) -> List[int]:
            m = len(p)
            # failure function
            fail = [0] * m
            j = 0
            for i in range(1, m):
                while j and p[i] != p[j]:
                    j = fail[j - 1]
                if p[i] == p[j]:
                    j += 1
                fail[i] = j
            # scan the text
            res = []
            j = 0
            for i, ch in enumerate(s):
                while j and ch != p[j]:
                    j = fail[j - 1]
                if ch == p[j]:
                    j += 1
                if j == m:
                    res.append(i - m + 1)
                    j = fail[j - 1]
            return res

        A = occurrences(a)
        B = occurrences(b)

        res = []
        p = 0
        for i in A:
            while p < len(B) and B[p] < i - k:
                p += 1
            if p < len(B) and B[p] <= i + k:
                res.append(i)
        return res
