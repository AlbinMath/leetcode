from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
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

        parent = list(range(M + 1))      # nodes are values/primes up to M

        def find(a: int) -> int:
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for v in nums:
            x = v
            while x > 1:
                p = spf[x]
                union(v, p)
                while x % p == 0:
                    x //= p

        count = {}
        best = 0
        for v in nums:
            r = find(v)
            count[r] = count.get(r, 0) + 1
            best = max(best, count[r])
        return best
