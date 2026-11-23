from typing import List
from bisect import bisect_left

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        R = [0] * n
        zeros = ones = 0
        j = 0  # window is [i, j), j exclusive
        for i in range(n):
            while j < n:
                z = zeros + (s[j] == '0')
                o = ones + (s[j] == '1')
                if z <= k or o <= k:
                    zeros, ones = z, o
                    j += 1
                else:
                    break
            R[i] = j - 1
            if s[i] == '0':
                zeros -= 1
            else:
                ones -= 1

        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + (R[i] - i + 1)

        ans = []
        for l, r in queries:
            p = bisect_left(R, r, l, r + 1)   # first i in [l, r] with R[i] >= r
            m = r - p + 1
            ans.append(pre[p] - pre[l] + m * (m + 1) // 2)
        return ans
