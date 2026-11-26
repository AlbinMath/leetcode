from bisect import bisect_left
from collections import defaultdict

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        T1 = s.count('1')
        T0 = n - T1

        P = [0] * (n + 1)
        pos = defaultdict(list)
        pos[0].append(0)
        for i, ch in enumerate(s):
            P[i + 1] = P[i] + (1 if ch == '1' else -1)
            pos[P[i + 1]].append(i + 1)

        res = 0
        for d, cap in ((0, n), (2, 2 * T0), (-2, 2 * T1)):
            for j in range(1, n + 1):
                lst = pos.get(P[j] - d)
                if not lst:
                    continue
                lo = max(0, j - cap)
                k = bisect_left(lst, lo)
                if k < len(lst) and lst[k] < j:
                    res = max(res, j - lst[k])
        return res
