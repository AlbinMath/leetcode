from typing import List

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        N = 10**4 + 20

        fact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv = [1] * (N + 1)
        inv[N] = pow(fact[N], MOD - 2, MOD)
        for i in range(N, 0, -1):
            inv[i - 1] = inv[i] * i % MOD

        def comb(a: int, b: int) -> int:
            return fact[a] * inv[b] % MOD * inv[a - b] % MOD

        ans = []
        for n, k in queries:
            res = 1
            p = 2
            while p * p <= k:
                if k % p == 0:
                    e = 0
                    while k % p == 0:
                        k //= p
                        e += 1
                    res = res * comb(e + n - 1, e) % MOD
                p += 1
            if k > 1:                       # one leftover prime, exponent 1
                res = res * comb(n, 1) % MOD
            ans.append(res)
        return ans
