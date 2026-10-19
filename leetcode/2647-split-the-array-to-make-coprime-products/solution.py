from typing import List

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        M = max(nums)

        # smallest prime factor sieve
        spf = list(range(M + 1))
        i = 2
        while i * i <= M:
            if spf[i] == i:
                for j in range(i * i, M + 1, i):
                    if spf[j] == j:
                        spf[j] = i
            i += 1

        first, last = {}, {}
        for idx, v in enumerate(nums):
            while v > 1:
                p = spf[v]
                while v % p == 0:
                    v //= p
                if p not in first:
                    first[p] = idx
                last[p] = idx

        diff = [0] * (n + 1)
        for p, f in first.items():
            l = last[p]
            if l > f:
                diff[f] += 1          # splits f .. l-1 are blocked
                diff[l] -= 1

        cover = 0
        for i in range(n - 1):
            cover += diff[i]
            if cover == 0:
                return i
        return -1
