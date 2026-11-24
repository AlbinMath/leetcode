from typing import List
from collections import Counter

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        k = 0
        A, B = Counter(), Counter()
        for c in cards:
            if c == x + x:
                k += 1
            elif c[0] == x:
                A[c[1]] += 1
            elif c[1] == x:
                B[c[0]] += 1

        def solve(cnt):
            s = sum(cnt.values())
            if s == 0:
                return 0, 0
            m = max(cnt.values())
            p = min(s // 2, s - m)
            return p, s - 2 * p

        pa, la = solve(A)
        pb, lb = solve(B)
        pairs = pa + pb
        ans = pairs

        use = min(k, la + lb)       # xx pairs with leftover cards
        ans += use
        k -= use

        ans += min(k // 2, pairs)   # 2 xx break a pair into two pairs
        return ans
