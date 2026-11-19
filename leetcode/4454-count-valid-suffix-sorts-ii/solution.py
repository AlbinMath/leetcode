import random
from typing import List

class Solution:
    def countSuffix(self, nums: List[int], target: List[int]) -> List[int]:
        n, m = len(nums), len(target)
        M = (1 << 64) - 1
        rnd = {}
        def h(v):
            if v not in rnd:
                rnd[v] = random.getrandbits(64)
            return rnd[v]

        total = 0
        for v in nums:
            total = (total + h(v)) & M
        T = [0] * (m + 1)
        for i, v in enumerate(target):
            T[i + 1] = (T[i] + h(v)) & M
        s = nums + [0] + target
        L = len(s)
        z = [0] * L
        l = r = 0
        for i in range(1, L):
            if i < r:
                z[i] = min(r - i, z[i - l])
            while i + z[i] < L and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] > r:
                l, r = i, i + z[i]
        st = [0] * m
        for p in range(1, m):
            st[p] = st[p - 1] if target[p] <= target[p - 1] else p

        ans = []
        for k in range(m - n + 1):
            if (T[k + n] - T[k]) & M != total:
                ans.append(0)
                continue
            e = k + n - 1
            lo = max(0, st[e] - k)
            hi = min(z[n + 1 + k], n - 1)
            ans.append(max(0, hi - lo + 1))
        return ans
